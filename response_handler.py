import copy

import user_input_handler

# Consts.
DEFAULT_CONFIG_KEY = "default"

COCO_STANDARD_RESPONSE = {
    "action_name": None,
    "component_done": False,  # Bool
    "component_failed": False,  # Bool
    "confidence": 1.0,
    "out_of_context": False,  # Bool
    "response": "",
    "response_time": 0.0,
    "updated_context": {}
}


class ResponseHandlerException(Exception):
    pass


# functions
def handle(component_id, cognigy_json_response, response_time_seconds=0.0):
    """
    Receives a Cognigy JSON result and formats it to a standard CoCo
    component response format.

    Arguments:
        component_id (string): Target Cognigy component ID, Cognigy bot endpoint
         URL.
        cognigy_json_response (dict): Cognigy JSON response.
        response_time_seconds (float): The time between the request and when
        the response was received.

    Returns:
        Result in a CoCo standard format. (dict)
    """
    coco_standard_response = copy.deepcopy(COCO_STANDARD_RESPONSE)

    response = cognigy_json_response.get("text", "")

    coco_standard_response["action_name"] = user_input_handler.fetch_action_name(
        response)

    coco_standard_response.update(user_input_handler.calculate_status_flags(
        response))

    coco_standard_response["response"] = \
        user_input_handler.clean_placeholders_from_text(response)

    coco_standard_response["response_time"] = response_time_seconds

    return coco_standard_response
