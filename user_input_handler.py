import copy
import re


# Consts.
STATUS_FLAGS = {
    "component_done": "done",
    "component_failed": "failed",
    "out_of_context":  "out_of_context"
}

PLACEHOLDER_REGEX = "\<(.*?)\>"
PLACEHOLDER_CONTENT_DELIMITER = ':'
ACTION_TAG = "action"


def _fetch_placeholders(text):
    """
    Fetch all placeholders tag content.
    Arguments:
        text: User input.

    Returns:
        Fetch placeholders (dict)
    """
    placeholders = {}
    regex = re.compile(PLACEHOLDER_REGEX)
    placeholder_contents = regex.findall(text)

    for content in placeholder_contents:
        if PLACEHOLDER_CONTENT_DELIMITER in content:
            tag, tag_value = content.split(PLACEHOLDER_CONTENT_DELIMITER)
            placeholders.update({tag: tag_value})
        else:
            placeholders.update({content: None})

    return placeholders


def fetch_action_name(text):
    """
    Arguments:
        text (string): User input.
    Returns:
        The action name if set, if not return None(string/ bool)
    """
    placeholders = _fetch_placeholders(text)

    return placeholders.get(ACTION_TAG)


def calculate_status_flags(text):
    """
    Check the status of the context text by looking for placeholder.
    Arguments:
        text (string): User input.
    Returns:
        Dict with context statuses (dict).
    """
    status_flags = copy.deepcopy(STATUS_FLAGS)

    placeholders = _fetch_placeholders(text)

    for flag, flag_placeholder in STATUS_FLAGS.items():
        status_flags[flag] = (flag_placeholder in placeholders.keys())

    return status_flags


def clean_placeholders_from_text(text):
    """
    Remove the placeholder from the context text.
    Arguments:
        text (string): User input.

    Returns:
        The text without the tag (string).
    """
    regex = re.compile(PLACEHOLDER_REGEX)
    placeholder_contents = regex.findall(text)

    for content in placeholder_contents:
        text = text.replace(f"<{content}>", "")

    return text


