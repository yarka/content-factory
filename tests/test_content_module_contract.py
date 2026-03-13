from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ContentModuleContractTests(unittest.TestCase):
    def test_content_module_files_exist(self) -> None:
        expected_paths = [
            "content/README.md",
            "content/accounts/.gitkeep",
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
            "content/workflows/linkedin-visual.md",
            "content/workflows/telegram-post.md",
            "content/workflows/adapters/telegram.md",
            "content/workflows/adapters/linkedin.md",
            "content/workflows/adapters/threads.md",
            "content/templates/linkedin-visual-card.html",
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
            "content/accounts/<account-slug>/posts/",
            "Saved to content/accounts/<account-slug>/posts/",
            "generate/refine LinkedIn visual",
            "review final text once with visual context",
            "publish",
            "content/workflows/fact-check.md",
            "content/workflows/deaify-text.md",
            "content/workflows/adapters/",
            "human_in_the_loop",
            "fully_automatic",
            "Depth Check",
            "If `human_in_the_loop` is enabled",
            "Quality Report",
            "fact-check",
            "deaify",
            "what changed",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

        self.assertNotIn("output/posts/", text)

    def test_config_example_exposes_content_workflow_mode(self) -> None:
        text = (ROOT / "config/config.example.yaml").read_text()

        required_snippets = [
            "workflow_mode:",
            "human_in_the_loop",
            "fully_automatic",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_linkedin_visual_workflow_requires_manual_references_before_visual_dna(self) -> None:
        text = (ROOT / "content/workflows/linkedin-visual.md").read_text()

        required_snippets = [
            "visual-reference-board.md",
            "visual-dna.md",
            "manual reference pack",
            "Do not lock a color/style direction before references exist",
            "content/accounts/<account-slug>/visuals/linkedin/",
            "single-image editorial card",
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
