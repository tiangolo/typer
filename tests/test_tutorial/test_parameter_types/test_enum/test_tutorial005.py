import subprocess

import typer
from typer.testing import CliRunner

from docs_src.parameter_types.enum import tutorial005 as mod

runner = CliRunner()

app = typer.Typer()
app.command()(mod.main)


def test_int_enum():
    result = runner.invoke(app, ["--access", "open"])
    assert result.exit_code == 0
    assert "Access level: open" in result.output


def test_script():
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
