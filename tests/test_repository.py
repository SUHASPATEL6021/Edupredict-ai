"""Small dependency-free repository smoke checks."""
import ast
import csv
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class RepositorySmokeTests(unittest.TestCase):
    def test_app_parses(self):
        ast.parse((ROOT / "app.py").read_text(encoding="utf-8"))

    def test_dependencies_and_documentation_exist(self):
        for name in ("requirements.txt", "README.md", "LICENSE", ".streamlit/config.toml"):
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).is_file())

    def test_sample_files_nonempty(self):
        samples = list((ROOT / "sample_data").glob("*"))
        self.assertTrue(samples)
        for sample in samples:
            with self.subTest(sample=sample.name):
                self.assertTrue(sample.read_text(encoding="utf-8").strip())

if __name__ == "__main__":
    unittest.main()
