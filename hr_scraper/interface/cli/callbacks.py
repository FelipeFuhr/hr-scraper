# -*- coding: utf-8 -*-
"""
Implements console callbacks
"""
from pathlib import Path

from typer import echo


def version(value: bool) -> None:
    """
    Callback for showing application version .

    Parameters
    ----------
    value : bool
        Necessary for typer to work properly, even if it is not set .

    Returns
    -------
    None

    """
    if value:
        version_callback()
    exit(0)


def version_callback() -> None:
    """
    Callback for showing application version .

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    version_path = Path(__file__).parent / "VERSION"
    with open(version_path, mode="r") as file:
        version = file.read()
        echo(f"Current version: {version}")
    return
