# -*- coding: utf-8 -*-
"""
Implements main function as cli functionalities .
"""
from typing import Optional

from pyfiglet import Figlet
from typer import Option, Typer

from data_service.commands import generate
from data_service.interface.cli.callbacks import version
from data_service.logger import logger

# application exposes the application with typer
application = Typer(help="Wraps AutoSklearn .")


@application.callback()
def main(
    version: Optional[bool] = Option(
        None,
        "--version",
        callback=version,
        is_eager=True,
        help=("Shows application version ."),
    ),
) -> None:
    """
    Initializes console and its functionalities .

    Parameters
    ----------
    version : Optional[bool]
        Callback that return application version .

    Returns
    -------
    None

    """
    print(Figlet().renderText("AutoSklearn Wrapper"))
    return


@application.command("generate")
def generate_cli(
    definition_path: str = Option(
        ..., "--definition-path", "-dp", help=("Path to the definition .")
    ),
    destination: str = Option(
        ..., "--destination", "-d", help=("Destination to save the Dataset .")
    ),
    dataset_name: str = Option(
        "dataset",
        "--dataset-name",
        "-dsn",
        help=("Name of the dataset file to be saved ."),
    ),
    save_definition: str = Option(
        True,
        "--save-definition",
        "-sdf",
        help=("Whether to save definition or not ."),
    ),
    definition_name: str = Option(
        "definition",
        "--definition-name",
        "-dfn",
        help=("Name of the definition artifact file to be saved ."),
    ),
    save_description: str = Option(
        True,
        "--save-description",
        "-sds",
        help=("Whether to save description or not ."),
    ),
    description_name: str = Option(
        "description",
        "--description-name",
        "-dsn",
        help=("Name of the description artifact file to be saved ."),
    ),
    save_logs: str = Option(
        True, "--save-logs", "-sl", help=("Whether to save logs or not .")
    ),
    logs_name: str = Option(
        "logs",
        "--logs-name",
        "-ln",
        help=("Name of the logs artifact file to be saved ."),
    ),
    file_format: str = Option(
        "parquet",
        "--file-format",
        "-ff",
        help=("File format to save dataset ."),
    ),
    seed: str = Option(42, "--seed", "-s", help=("Seed .")),
):
    """
    Generates Dataset .

    Parameters
    ----------
    definition_path: str
        Path with the definition .
    destination: str
        Base path to save artifacts .
    dataset_name: Optional[str]
        Dataset name .
    save_definition: Optional[bool]
        Whether to save definition of not .
    definition_name: Optional[str]
        If save_definition is True, saves definition with name
        given by this variable .
    save_description: Optional[bool]
        Whether to save description of not .
    description_name: Optional[str]
        If save_description is True, saves description with name
        given by this variable .
    save_logs: Optional[bool]
        Whether to save logs of not .
    logs_name: Optional[str]
        If save_logs is True, saves logs with name
        given by this variable .
    file_format: Optional[str]
        File format to save dataset .
    seed: Optional[int]
        Random seed to be set for reproducibility .

    Returns
    -------
    None

    """
    logger.debug("Entered cli's generate command .")
    generate(
        definition_path=definition_path,
        destination=destination,
        dataset_name=dataset_name,
        save_definition=save_definition,
        definition_name=definition_name,
        save_description=save_description,
        description_name=description_name,
        save_logs=save_logs,
        logs_name=logs_name,
        file_format=file_format,
        seed=seed,
    )


if __name__ == "__main__":
    application()
