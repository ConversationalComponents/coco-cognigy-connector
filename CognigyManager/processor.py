import requests
import logging
import json
import os

from .custom_exceptions import LoadComponentError

COMPONENTS_FOLDER_NAME = "components"


def _build_client_config_path(component_id):
    """
    Build service account json file full path.

    Arguments:
        component_id (string): Target Cognigy component ID, Cognigy bot endpoint URL.

    Returns:
        Client config file path (string)
    """
    components_folder_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), COMPONENTS_FOLDER_NAME)
    return f"{components_folder_name}/{component_id}.json"


def _load_client_config(component_id):
    """
    Fetch service account json content.

    Arguments:
        component_id (string): Target Cognigy component ID, Cognigy bot endpoint URL.

    Returns:
         Client config file json content. (dict)
    """

    config_file_path = _build_client_config_path(component_id)

    if not os.path.isfile(config_file_path):
        error_message = f"Component with ID: {component_id} does not exist."
        logging.error(error_message)
        raise LoadComponentError(error_message)

    with open(config_file_path, "rb") as f:
        return json.loads(f.read())


def process_request(component_id, session_id, text, language_code="en"):
    """
    Returns bot output for user input.

    Using the same `session_id` between requests allows continuation
    of the conversation.

    Arguments:
        component_id (string): Target Cognigy component ID, Cognigy bot endpoint URL.
        session_id (string): Unique session for context user.
        text (string): User input.
        language_code (string): Context language.
    Returns:
        Cognigy JSON response. (dict)
    """
    bot_config = _load_client_config(component_id)

    endpoint_url = bot_config["endpoint_url"]

    response = requests.post(endpoint_url, json={
        "userId": session_id,
        "sessionId": session_id,
        "text": text
    })

    response.raise_for_status()

    return response.json()
