import os
import logging
import json
import sys

from datetime import datetime

from utils.common import is_enabled

LOG_LEVEL = os.environ['LOG_LEVEL']
LOG_FORMAT = os.getenv('LOG_FORMAT')

def is_level_partof(level, levels):
    return any(l == "{}".format(level).lower() for l in levels)

def is_debug(level):
    return is_level_partof(level, ["debug", "notice"])

def is_warn(level):
    return is_level_partof(level, ["warning", "warn"])

def is_error(level):
    return is_level_partof(level, ["error", "fatal", "crit"])

if is_debug(LOG_LEVEL):
    logging.basicConfig(stream = sys.stdout, level = "DEBUG")
elif is_warn(LOG_LEVEL):
    logging.basicConfig(stream = sys.stdout, level = "WARNING")
elif is_error(LOG_LEVEL):
    logging.basicConfig(stream = sys.stderr, level = "ERROR")
else:
    logging.basicConfig(stream = sys.stdout, level = "INFO")

def log_msg (log_level, message):
    vdate = datetime.now().isoformat()
    formatted_log = "[{}][{}] {}".format(log_level, vdate, message)
    if is_enabled(LOG_FORMAT) and LOG_FORMAT == "json":
        if isinstance(message, dict):
            message['level'] = log_level
            message['time'] = vdate
            formatted_log = json.dumps(message)
        else:
            formatted_log = json.dumps({"body": message, "level": log_level, "time": vdate})

    if is_debug(log_level):
        logging.debug(formatted_log)
    elif is_warn(log_level):
        logging.warning(formatted_log)
    elif is_error(log_level):
        logging.error(formatted_log)
    else:
        logging.info(formatted_log)
