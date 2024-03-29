from datetime import datetime

import typer
from typing_extensions import Annotated


def main(
    launch_date: Annotated[
        datetime,
        typer.Argument(
            formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y"]
        ),
    ],
):
    print(f"Launch will be at: {launch_date}")


if __name__ == "__main__":
    typer.run(main)
