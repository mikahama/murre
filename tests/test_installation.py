"""Run against an installed distribution, without loading or downloading models."""

import importlib
import importlib.metadata
import re
import socket
import unittest
from unittest.mock import patch


class InstallationTest(unittest.TestCase):
    def test_runtime_dependencies_are_declared(self):
        requirements = importlib.metadata.requires("murre") or []
        names = {
            re.match(r"[\w.-]+", requirement).group().lower().replace("_", "-")
            for requirement in requirements
        }
        self.assertTrue({"mikatools", "onmt-runner"} <= names, requirements)
        self.assertTrue(names.isdisjoint({"natas", "opennmt-py"}), requirements)

    def test_public_imports_without_models_or_network(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("Network access during import")), patch.object(
            socket, "create_connection", side_effect=AssertionError("Network access during import")
        ):
            import murre
            import mikatools
            from onmt_runner import Translator

            normalizer = importlib.import_module("murre.normalizer")
            generator = importlib.import_module("murre.generator")
            downloader = importlib.import_module("murre.download")
            for name in (
                "normalize_sentence", "normalize_sentences", "dialectalize_sentence",
                "dialectalize_sentences", "supported_dialects",
            ):
                self.assertTrue(callable(getattr(murre, name)), name)
            self.assertTrue(murre.supported_dialects())
            self.assertIs(normalizer.Translator, Translator)
            self.assertIs(generator.Translator, Translator)
            self.assertEqual(normalizer.models, {})
            self.assertIsNone(generator.model)
            self.assertTrue(callable(mikatools.script_path))
            self.assertTrue(callable(mikatools.download_file))
            self.assertTrue(callable(downloader.main))


if __name__ == "__main__":
    unittest.main()
