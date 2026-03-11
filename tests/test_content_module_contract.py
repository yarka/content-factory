from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ContentModuleContractTests(unittest.TestCase):
    def test_content_module_files_exist(self) -> None:
        expected_paths = [
            "content/README.md",
            "content/channel-dna.md",
            "content/channel-dna-linkedin.md",
            "content/channel-dna.template.md",
            "content/writing-guide.md",
            "content/writing-guide.template.md",
            "content/ai-terms-ru.md",
            "content/workflows/core-pipeline.md",
            "content/workflows/fact-check.md",
            "content/workflows/deaify-text.md",
            "content/workflows/blog-post.md",
            "content/workflows/telegram-post.md",
            "content/workflows/adapters/telegram.md",
            "content/workflows/adapters/linkedin.md",
            "content/workflows/adapters/threads.md",
        ]

        for relative_path in expected_paths:
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_core_pipeline_reads_new_module_paths(self) -> None:
        text = (ROOT / "content/workflows/core-pipeline.md").read_text()

        required_snippets = [
            "content/channel-dna.md",
            "content/writing-guide.md",
            "strategy/accounts/<account-slug>/content-plan.yaml",
            "intelligence/accounts/<account-slug>/intelligence-snapshot.yaml",
            "content/workflows/fact-check.md",
            "content/workflows/deaify-text.md",
            "content/workflows/adapters/",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_old_flat_content_paths_are_removed(self) -> None:
        old_paths = [
            "channel-dna.md",
            "channel-dna-linkedin.md",
            "channel-dna.template.md",
            "rules/core-pipeline.md",
            "rules/fact-check.md",
            "rules/deaify-text.md",
            "rules/blog-post.md",
            "rules/telegram-post.md",
            "rules/adapters/telegram.md",
            "rules/adapters/linkedin.md",
            "rules/adapters/threads.md",
            "rules/ai-terms-ru.md",
            "rules/writing-guide.md",
            "rules/writing-guide.template.md",
        ]

        for relative_path in old_paths:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)


if __name__ == "__main__":
    unittest.main()
