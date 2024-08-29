from typing import List

import pytest
import typer
import typer.completion
from typer.testing import CliRunner

runner = CliRunner()
rounded = ["╭", "─", "┬", "╮", "│", "├", "┼", "┤", "╰", "┴", "╯"]


def test_rich_markup_mode_none():
    app = typer.Typer(rich_markup_mode=None)

    @app.command()
    def main(arg: str):
        """Main function"""
        print(f"Hello {arg}")

    assert app.rich_markup_mode is None

    result = runner.invoke(app, ["World"])
    assert "Hello World" in result.stdout

    result = runner.invoke(app, ["--help"])
    assert all(c not in result.stdout for c in rounded)


def test_rich_markup_mode_rich():
    app = typer.Typer(rich_markup_mode="rich")

    @app.command()
    def main(arg: str):
        """Main function"""
        print(f"Hello {arg}")

    assert app.rich_markup_mode == "rich"

    result = runner.invoke(app, ["World"])
    assert "Hello World" in result.stdout

    result = runner.invoke(app, ["--help"])
    assert any(c in result.stdout for c in rounded)


@pytest.mark.parametrize(
    "mode,lines",
    [
        ("markdown", ["First line", "", "Line 1", "", "Line 2", ""]),
        ("rich", ["First line", "", "Line 1", "", "Line 2", ""]),
        ("none", ["First line", "", "Line 1", "Line 2", ""]),
    ],
)
def test_markup_mode_newline_pr815(mode: str, lines: List[str]):
    app = typer.Typer(rich_markup_mode=mode)

    @app.command()
    def main():
        """First line

        Line 1

        Line 2
        """
        pass

    assert app.rich_markup_mode == mode

    result = runner.invoke(app, ["--help"])
    result_lines = [line.strip() for line in result.stdout.split("\n")]
    assert any(c in result.stdout for c in rounded)
    help_start = result_lines.index("First line")
    options_start = [i for i, row in enumerate(result_lines) if "Options" in row][0]
    assert help_start != -1
    assert result_lines[help_start:options_start] == lines


@pytest.mark.parametrize(
    "mode,lines",
    [
        ("markdown", ["First line", "", "Line 1 Line 2 Line 3", ""]),
        ("rich", ["First line", "", "Line 1", "Line 2", "Line 3", ""]),
        ("none", ["First line", "", "Line 1 Line 2 Line 3", ""]),
    ],
)
def test_markup_mode_newline_issue447(mode: str, lines: List[str]):
    app = typer.Typer(rich_markup_mode=mode)

    @app.command()
    def main():
        """First line

        Line 1
        Line 2
        Line 3
        """
        pass

    assert app.rich_markup_mode == mode

    result = runner.invoke(app, ["--help"])
    result_lines = [line.strip() for line in result.stdout.split("\n")]
    assert any(c in result.stdout for c in rounded)
    help_start = result_lines.index("First line")
    options_start = [i for i, row in enumerate(result_lines) if "Options" in row][0]
    assert help_start != -1
    assert result_lines[help_start:options_start] == lines