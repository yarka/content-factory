from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SetupModuleContractTests(unittest.TestCase):
    def test_setup_module_files_exist(self) -> None:
        expected_paths = [
            "setup/README.md",
            "setup/bootstrap.md",
        ]

        for relative_path in expected_paths:
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_old_setup_path_is_removed(self) -> None:
        self.assertFalse((ROOT / "rules/setup.md").exists())


if __name__ == "__main__":
    unittest.main()
