# -*- coding: utf-8 -*-
from flask import Flask

from data_service.commands import generate
from data_service.logger import logger

application = Flask(__name__)


@application.route("/generate", methods=["POST"])
def generate_call(request):
    if request.method == "POST":
        data = request.get_json()
        definition_path = data["definition_path"]
        destination = data["destination"]
        dataset_name = data["dataset_name"]
        save_definition = data["save_definition"]
        definition_name = data["definition_name"]
        save_description = data["save_description"]
        description_name = data["description_name"]
        save_logs = data["save_logs"]
        logs_name = data["logs_name"]
        file_format = data["file_format"]
        seed = data["seed"]
        logger.debug("Entered api's generate command .")
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
    application.run()
