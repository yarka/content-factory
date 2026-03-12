from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class IntelligenceModuleContractTests(unittest.TestCase):
    def test_intelligence_workspace_templates_exist(self) -> None:
        expected_paths = [
            "intelligence/README.md",
            "intelligence/accounts/.gitkeep",
            "intelligence/templates/source-config.template.yaml",
            "intelligence/templates/manual-context.template.md",
            "intelligence/templates/discovered-sources.template.yaml",
            "intelligence/templates/evidence-log.template.yaml",
            "intelligence/templates/intelligence-snapshot.template.yaml",
            "intelligence/templates/coverage-report.template.yaml",
            "intelligence/templates/research-report.template.md",
            "intelligence/workflows/discovery.md",
            "intelligence/workflows/refresh.md",
            "docs/INTELLIGENCE_TEST_CASES.md",
        ]

        for relative_path in expected_paths:
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_source_config_template_captures_upstream_inputs(self) -> None:
        text = (ROOT / "intelligence/templates/source-config.template.yaml").read_text()

        required_fields = [
            "account_slug:",
            "business_context:",
            "platform_focus:",
            "search_constraints:",
            "manual_context_sources:",
            "external_data_sources:",
            "source_tiers:",
            "tier_1:",
            "tier_2_extensions:",
        ]

        for field in required_fields:
            self.assertIn(field, text)

    def test_evidence_log_template_requires_normalized_evidence_records(self) -> None:
        text = (ROOT / "intelligence/templates/evidence-log.template.yaml").read_text()

        required_fields = [
            "evidence_id:",
            "source_family:",
            "source_type:",
            "source_origin:",
            "acquisition_mode:",
            "strategy_type:",
            "entity_id:",
            "url:",
            "summary:",
            "confidence:",
            "discussion_signals:",
        ]

        for field in required_fields:
            self.assertIn(field, text)

    def test_snapshot_template_captures_four_search_strategies_and_fallbacks(self) -> None:
        text = (ROOT / "intelligence/templates/intelligence-snapshot.template.yaml").read_text()

        required_fields = [
            "direct_competitor_discovery:",
            "adjacent_analog_discovery:",
            "audience_pain_discovery:",
            "winning_content_discovery:",
            "competitor_universe:",
            "pattern_library:",
            "fallback_notes:",
            "stable_snapshot_id:",
        ]

        for field in required_fields:
            self.assertIn(field, text)

    def test_quality_gate_templates_capture_research_status_and_reports(self) -> None:
        coverage = (ROOT / "intelligence/templates/coverage-report.template.yaml").read_text()
        report = (ROOT / "intelligence/templates/research-report.template.md").read_text()

        coverage_fields = [
            "status:",
            "recommendation:",
            "entity_count:",
            "evidence_count:",
            "coverage_by_strategy:",
            "coverage_by_source_family:",
            "confidence_summary:",
            "gaps:",
        ]

        for field in coverage_fields:
            self.assertIn(field, coverage)

        report_sections = [
            "## Executive Summary",
            "## Competitor Universe",
            "## Buyer Pain Language",
            "## Winning Patterns",
            "## Strategic Implications",
            "## What Is Still Missing",
        ]

        for section in report_sections:
            self.assertIn(section, report)

    def test_discovery_rule_defines_tiered_sources_and_four_search_strategies(self) -> None:
        text = (ROOT / "intelligence/workflows/discovery.md").read_text()

        required_snippets = [
            "Exa MCP",
            "preferred discovery engine",
            "Web search fallback",
            "Always save the discovery artifacts",
            "research-report.md",
            "coverage-report.yaml",
            "warning_needs_enrichment",
            "12-15 discovered entities",
            "25-40 evidence records",
            "Direct competitor discovery",
            "Adjacent analog discovery",
            "Audience pain discovery",
            "Winning-content discovery",
            "Tier 1 sources",
            "LinkedIn",
            "Reddit",
            "websites/blogs",
            "Tier 2 extensions",
            "discussion language",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_readme_documents_auto_saved_artifacts_and_external_sources(self) -> None:
        text = (ROOT / "intelligence/README.md").read_text()

        required_snippets = [
            "saved by default",
            "external_data_sources",
            "private_market_signal",
            "upwork_manual_export",
            "coverage-report.yaml",
            "research-report.md",
            "ready_for_strategy",
            "warning_needs_enrichment",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_refresh_rule_updates_snapshot_without_changing_strategy_layer_directly(self) -> None:
        text = (ROOT / "intelligence/workflows/refresh.md").read_text()

        required_snippets = [
            "compare against the previous snapshot",
            "fallback",
            "Do not update strategy artifacts directly",
            "refresh report",
        ]

        for snippet in required_snippets:
            self.assertIn(snippet, text)

    def test_docs_advertise_intelligence_triggers(self) -> None:
        readme = (ROOT / "README.md").read_text().lower()
        claude = (ROOT / "CLAUDE.md").read_text().lower()

        for snippet in ["run intelligence", "refresh intelligence"]:
            self.assertIn(snippet, readme)
            self.assertIn(snippet, claude)

        for snippet in [
            "start linkedin pilot",
            "continue linkedin pilot",
            "review intelligence coverage",
        ]:
            self.assertIn(snippet, readme)
            self.assertIn(snippet, claude)

    def test_old_flat_intelligence_paths_are_removed(self) -> None:
        old_paths = [
            "rules/intelligence-discovery.md",
            "rules/intelligence-refresh.md",
        ]

        for relative_path in old_paths:
            self.assertFalse((ROOT / relative_path).exists(), relative_path)


if __name__ == "__main__":
    unittest.main()
