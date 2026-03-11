#!/usr/bin/env python3
"""
Публикация поста в LinkedIn через Chrome.

Использование:
  python3 publish/publish_linkedin.py --file output/posts/YYYY-MM-DD-slug.md
  python3 publish/publish_linkedin.py --setup   # первичный логин
"""

import argparse
import sys
from pathlib import Path

# Отдельный профиль для постинга (сохраняет сессию LinkedIn)
PUBLISHER_PROFILE = str(Path.home() / ".linkedin-publisher")


def read_post(file_path):
    content = Path(file_path).read_text().strip()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    return content


def launch_context(p):
    return p.chromium.launch_persistent_context(
        user_data_dir=PUBLISHER_PROFILE,
        channel="chrome",
        headless=False,
        args=["--no-first-run"],
    )


def setup_profile():
    """Первичная настройка — открывает Chrome, ждёт логина автоматически."""
    from playwright.sync_api import sync_playwright

    print("🔑 Открываю Chrome — залогинься в LinkedIn.")
    print("   Скрипт сам закроется когда увидит что ты залогинен.")
    with sync_playwright() as p:
        context = launch_context(p)
        page = context.new_page()
        page.goto("https://www.linkedin.com/login")
        # Ждём пока URL не станет фидом (залогинился)
        page.wait_for_url("**/feed/**", timeout=120000)
        print("\n✅ Залогинен! Сохраняю профиль...")
        page.wait_for_timeout(1000)
        context.close()
    print("✅ Профиль сохранён. Теперь можно публиковать.")


def publish(post_text: str):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        print("🌐 Открываю Chrome...")
        context = launch_context(p)
        page = context.new_page()
        page.set_viewport_size({"width": 1440, "height": 900})

        print("📎 Открываю LinkedIn...")
        page.goto("https://www.linkedin.com/feed/", wait_until="domcontentloaded")
        page.wait_for_timeout(2000)

        # Если не залогинен — ждём
        if "login" in page.url or "authwall" in page.url or "checkpoint" in page.url:
            print("\n⚠️  Не залогинен. Залогинься в браузере, потом нажми Enter...")
            input()
            page.goto("https://www.linkedin.com/feed/", wait_until="domcontentloaded")
            page.wait_for_timeout(2000)

        # Шаг 1: пишем текст в clipboard из main frame (работает cross-frame)
        page.evaluate(f"navigator.clipboard.writeText({repr(post_text)})")

        # Шаг 2: кликаем "Start a post" / "Новая публикация" по координатам
        print("✏️  Открываю форму поста...")
        page.mouse.click(600, 140)
        page.wait_for_timeout(2500)

        # Шаг 3: клик в центр модала и Cmd+V (проверенный метод)
        print("📋 Вставляю текст...")
        page.mouse.click(716, 250)
        page.wait_for_timeout(800)
        page.keyboard.press("Meta+v")
        page.wait_for_timeout(1500)

        print("\n─────────────────────────────────")
        print("👀 Пост вставлен. Проверь глазами.")
        print("─────────────────────────────────")
        confirm = input("\nПостить? [y/N] ").strip().lower()

        if confirm != 'y':
            print("Отменено.")
            context.close()
            sys.exit(0)

        # Нажимаем Post
        print("🚀 Публикую...")
        try:
            page.get_by_role("button", name="Post", exact=True).click()
        except Exception:
            page.locator("button.share-actions__primary-action").click()

        page.wait_for_timeout(3000)
        print("✅ Опубликовано!")
        context.close()


def main():
    parser = argparse.ArgumentParser(description="Публикация поста в LinkedIn")
    parser.add_argument("--file", help="Путь к .md файлу с постом")
    parser.add_argument("--setup", action="store_true", help="Первичный логин в LinkedIn")
    args = parser.parse_args()

    if args.setup:
        setup_profile()
        return

    if not args.file:
        print("❌ Укажи файл: --file output/posts/FILE.md")
        sys.exit(1)

    post_text = read_post(args.file)
    if not post_text:
        print("❌ Пустой файл")
        sys.exit(1)

    print(f"📄 Файл: {args.file}")
    print(f"\n── Превью ──────────────────────")
    print(post_text[:300] + ("..." if len(post_text) > 300 else ""))
    print(f"────────────────────────────────")
    print(f"Символов: {len(post_text)}")

    confirm = input("\nЗапустить публикацию в LinkedIn? [y/N] ").strip().lower()
    if confirm != 'y':
        print("Отменено.")
        sys.exit(0)

    publish(post_text)


if __name__ == "__main__":
    main()
