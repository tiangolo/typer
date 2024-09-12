from enum import Enum
from typing import Tuple

import typer
from typing_extensions import Annotated


class SuperHero(str, Enum):
    hero1 = "Superman"
    hero2 = "Spiderman"
    hero3 = "Wonder woman"


def main(
    names: Annotated[
        Tuple[str, str, str, SuperHero],
        typer.Argument(enum_by_name=True, help="Select 4 characters to play with"),
    ] = ("Harry", "Hermione", "Ron", "hero3"),
):
    for name in names:
        print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
