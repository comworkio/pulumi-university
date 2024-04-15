import re
from time import sleep
from pulumi import automation as auto

from utils.logger import log_msg

_MAX_RETRY = 3
_WAIT_TIME = 2
_allowed_chars_pattern = re.compile(r'^[a-zA-Z0-9_\-\.]+$')

def is_valid_field(value):
    return bool(re.match(_allowed_chars_pattern, value))

def is_not_valid_field(value):
    return not is_valid_field(value)

def delete_resource(project, name, retry = 0):
    try:
        if retry >= _MAX_RETRY:
            log_msg("WARN", "[delete_resource] max retries has been reached : retry = {}, name = {}, environment = {}".format(retry, name, project))
            return

        if retry > 0:
            waiting_time = _WAIT_TIME * retry
            log_msg("DEBUG", "[delete_resource] waiting: name = {}, project = {}, wait = {}".format(name, project, waiting_time))
            sleep(waiting_time)

        stack = auto.select_stack(stack_name = name, project_name = project, program = delete_resource)
        stack.destroy()
    except Exception as e:
        log_msg("WARN", "[delete_resource] trying again because of this error: name = {}, project = {}, error = {}".format(name, project, e))
        delete_resource(project, name, retry + 1)
