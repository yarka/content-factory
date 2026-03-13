#!/usr/bin/env python3
"""
Публикация поста в Telegram.

Использование:
  python3 publish/publish.py                        # staging (по умолчанию)
  python3 publish/publish.py --env production       # прод
  python3 publish/publish.py --file content/accounts/ai-consulting-pilot/posts/2026-02-26-massazh.md
"""

import argparse
import sys
import yaml
import requests
import re
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config/config.yaml"


def load_config():
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def get_env_config(config, env=None):
    active_env = env or config.get("env", "staging")
    envs = config.get("environments", {})
    if active_env not in envs:
        print(f"❌ Окружение '{active_env}' не найдено в config.yaml")
        sys.exit(1)
    return active_env, envs[active_env]


def md_to_telegram_html(text):
    """Конвертирует Markdown-разметку в Telegram HTML."""
    # **bold** → <b>bold</b>
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # [text](url) → <a href="url">text</a>
    text = re.sub(r'\[(.+?)\]\((https?://[^\)]+)\)', r'<a href="\2">\1</a>', text)
    # Длинные тире → короткие
    text = text.replace('—', '–')
    return text


def read_post(file_path):
    """Читает .md файл, убирает frontmatter, возвращает текст."""
    content = Path(file_path).read_text()
    # Убираем frontmatter (---...---)
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    return md_to_telegram_html(content)


def send_message(token, channel_id, text, preview=True):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    resp = requests.post(url, json={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": not preview
    })
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Публикация поста в Telegram")
    parser.add_argument("--env", choices=["staging", "production"],
                        help="Окружение (по умолчанию из config.yaml)")
    parser.add_argument("--file", help="Путь к .md файлу с постом")
    parser.add_argument("--no-preview", action="store_true",
                        help="Отключить предпросмотр ссылок")
    args = parser.parse_args()

    config = load_config()
    env_name, env_config = get_env_config(config, args.env)

    token = env_config["bot_token"]
    channel_id = env_config["channel_id"]

    print(f"📡 Окружение: {env_name}")
    print(f"📢 Канал: {channel_id}")

    if args.file:
        text = read_post(args.file)
        print(f"📄 Файл: {args.file}")
    else:
        print("📝 Введи текст поста (Ctrl+D для завершения):")
        text = md_to_telegram_html(sys.stdin.read().strip())

    if not text:
        print("❌ Пустой текст")
        sys.exit(1)

    print(f"\n── Превью ──────────────────────")
    print(text[:300] + ("..." if len(text) > 300 else ""))
    print(f"────────────────────────────────")
    print(f"Символов: {len(text)}")

    confirm = input(f"\nОпубликовать в {env_name}? [y/N] ")
    if confirm.lower() != 'y':
        print("Отменено.")
        sys.exit(0)

    result = send_message(token, channel_id, text, preview=not args.no_preview)

    if result.get("ok"):
        msg_id = result["result"]["message_id"]
        print(f"✅ Опубликовано! message_id: {msg_id}")
    else:
        print(f"❌ Ошибка: {result['description']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
