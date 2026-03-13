from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublishModuleContractTests(unittest.TestCase):
    def test_publish_module_files_exist(self) -> None:
        expected_paths = [
            "publish/README.md",
            "publish/publish.py",
            "publish/publish_linkedin.py",
            "publish/workflows/publish.md",
            "publish/workflows/adapters/telegram.md",
            "publish/workflows/adapters/file-only.md",
            "publish/workflows/adapters/custom.md",
        ]

        for relative_path in expected_paths:
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_publish_router_references_module_owned_paths(self) -> None:
        text = (ROOT / "publish/workflows/publish.md").read_text()

        required_snippets = [
            "publish/workflows/adapters/telegram.md",
            "publish/workflows/adapters/file-only.md",
            "publish/workflows/adapters/custom.md",
            "config/config.yaml",
            "content/accounts/<account-slug>/posts/",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_publish_scripts_read_root_config_from_new_module(self) -> None:
        telegram_script = (ROOT / "publish/publish.py").read_text()
        linkedin_script = (ROOT / "publish/publish_linkedin.py").read_text()

        self.assertIn('Path(__file__).resolve().parents[1] / "config/config.yaml"', telegram_script)
        self.assertNotIn("output/posts", telegram_script)
        self.assertNotIn("output/posts", linkedin_script)

    def test_publish_docs_reference_content_account_artifacts_not_output_posts(self) -> None:
        readme = (ROOT / "publish/README.md").read_text()
        file_only = (ROOT / "publish/workflows/adapters/file-only.md").read_text()

        for text in [readme, file_only]:
            self.assertIn("content/accounts/<account-slug>/posts/", text)
            self.assertNotIn("output/posts", text)

    def test_old_publish_paths_are_removed(self) -> None:
        old_paths = [
            "publish.py",
            "publish_linkedin.py",
            "rules/publish/publish.md",
        ]

        for relative_path in old_paths:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)


if __name__ == "__main__":
    unittest.main()
