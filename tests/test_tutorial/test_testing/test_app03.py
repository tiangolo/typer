import subprocess
import sys

from docs_src.testing.app03 import main as mod
from docs_src.testing.app03.test_main import test_app


def test_app03():
    test_app()


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
