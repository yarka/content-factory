from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class LinkedInStrategistContractTests(unittest.TestCase):
    def test_strategy_workspace_templates_exist(self) -> None:
        expected_paths = [
            "strategy/README.md",
            "strategy/accounts/.gitkeep",
            "strategy/templates/account-profile.template.yaml",
            "strategy/templates/manual-context.template.md",
            "strategy/templates/content-plan.template.yaml",
            "strategy/templates/strategy-pack.template.md",
            "strategy/templates/refresh-report.template.md",
            "strategy/workflows/linkedin-strategist.md",
            "strategy/workflows/refresh.md",
        ]

        for relative_path in expected_paths:
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_account_profile_template_contains_required_business_brief_fields(self) -> None:
        text = (ROOT / "strategy/templates/account-profile.template.yaml").read_text()

        required_fields = [
            "business_category:",
            "primary_platform:",
            "goal_type:",
            "audience:",
            "offer_ladder:",
            "lead_magnet:",
            "proof_assets:",
            "positioning_seed:",
            "worldview_and_values:",
            "tone_constraints:",
            "manual_context_sources:",
        ]

        for field in required_fields:
            self.assertIn(field, text)

    def test_account_profile_template_supports_founder_systems_orchestrator_positioning(self) -> None:
        text = (ROOT / "strategy/templates/account-profile.template.yaml").read_text()

        required_snippets = [
            "founders with digital products",
            "personal brand",
            "brand_to_demand",
            "systems_orchestrator_identity",
            "founder_os_audit",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_content_plan_template_captures_post_and_image_brief_contracts(self) -> None:
        text = (ROOT / "strategy/templates/content-plan.template.yaml").read_text()

        required_fields = [
            "weekly_themes:",
            "post_briefs:",
            "image_brief:",
            "funnel_stage:",
            "pillar_tag:",
            "hook_direction:",
            "proof_asset:",
            "soft_cta_style:",
            "supporting_evidence_ids:",
            "visual_angle:",
            "composition_direction:",
            "text_overlay_guidance:",
            "style_constraints:",
            "no_go_list:",
        ]

        for field in required_fields:
            self.assertIn(field, text)

    def test_linkedin_strategist_rule_consumes_snapshot_and_builds_strategy_outputs(self) -> None:
        text = (ROOT / "strategy/workflows/linkedin-strategist.md").read_text()

        required_snippets = [
            "Read the business brief",
            "approved intelligence snapshot",
            "operator background",
            "orchestrator",
            "mission",
            "values",
            "Pattern Library",
            "Strategy Pack",
            "30-Day Plan",
            "Image Briefs",
            "profile packaging recommendations",
            "featured asset recommendations",
            "content series map",
            "what to copy vs what to reject",
            "Save all artifacts",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

        forbidden_snippets = [
            "Pull evidence from Exa",
            "Build competitor universe automatically",
        ]

        for snippet in forbidden_snippets:
            self.assertNotIn(snippet, text)

    def test_strategy_pack_template_supports_profile_and_competitor_adaptation_outputs(self) -> None:
        text = (ROOT / "strategy/templates/strategy-pack.template.md").read_text()

        required_sections = [
            "## Profile Packaging Recommendations",
            "## Featured Asset Recommendations",
            "## Content Series Map",
            "## Adapt vs Reject",
        ]

        for section in required_sections:
            self.assertIn(section, text)

    def test_refresh_rule_requires_delta_report_without_silent_overwrite(self) -> None:
        text = (ROOT / "strategy/workflows/refresh.md").read_text()

        required_snippets = [
            "rerun intelligence discovery",
            "compare against the previous snapshot",
            "Refresh Delta",
            "recommended adds/removals",
            "Do not silently overwrite",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_core_pipeline_supports_strategy_brief_handoff(self) -> None:
        text = (ROOT / "content/workflows/core-pipeline.md").read_text()

        required_snippets = [
            "selected strategy post brief",
            "image brief",
            "approved strategy constraints",
            "supporting evidence",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_docs_advertise_strategy_and_refresh_triggers(self) -> None:
        readme = (ROOT / "README.md").read_text()
        claude = (ROOT / "CLAUDE.md").read_text()

        expected_snippets = [
            "linkedin strategy",
            "refresh linkedin strategy",
        ]

        for snippet in expected_snippets:
            self.assertIn(snippet, readme.lower())
            self.assertIn(snippet, claude.lower())

    def test_old_flat_strategy_paths_are_removed(self) -> None:
        old_paths = [
            "rules/linkedin-strategist.md",
            "rules/linkedin-strategy-refresh.md",
        ]

        for relative_path in old_paths:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)


if __name__ == "__main__":
    unittest.main()
