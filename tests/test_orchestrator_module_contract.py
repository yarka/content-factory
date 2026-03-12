from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class OrchestratorModuleContractTests(unittest.TestCase):
    def test_orchestrator_module_files_exist(self) -> None:
        expected_paths = [
            "orchestrator/README.md",
            "orchestrator/workflows/start-linkedin-pilot.md",
            "orchestrator/workflows/continue-linkedin-pilot.md",
            "orchestrator/templates/pilot-status.template.yaml",
        ]

        for relative_path in expected_paths:
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_start_workflow_guides_user_through_full_linkedin_pilot(self) -> None:
        text = (ROOT / "orchestrator/workflows/start-linkedin-pilot.md").read_text()

        required_snippets = [
            "business brief",
            "optional private/manual sources",
            "run `intelligence`",
            "coverage report",
            "research report",
            "warning",
            "manual enrichment",
            "linkedin strategy",
            "write from strategy brief",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_orchestrator_status_template_defines_handoff_states(self) -> None:
        text = (ROOT / "orchestrator/templates/pilot-status.template.yaml").read_text()

        required_fields = [
            "status:",
            "ready_for_strategy",
            "warning_needs_enrichment",
            "blocked_missing_brief",
            "next_action:",
            "linked_artifacts:",
        ]

        for field in required_fields:
            self.assertIn(field, text)

    def test_old_flat_orchestrator_paths_do_not_exist(self) -> None:
        old_paths = [
            "rules/start-linkedin-pilot.md",
            "rules/continue-linkedin-pilot.md",
        ]

        for relative_path in old_paths:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)


if __name__ == "__main__":
    unittest.main()
