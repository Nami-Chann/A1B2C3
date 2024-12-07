import os
from database.database import get_variable

# Function to retrieve configuration values with a fallback to environment variables
def get_config_value(key: str, default: str):
    return get_variable(key, os.environ.get(key, default))

# Retrieve FORCE_SUB_CHANNEL values, with fallback to default environment values
FORCE_SUB_CHANNEL_1 = int(get_config_value("FORCE_SUB_CHANNEL_1", "-1002220717902"))
FORCE_SUB_CHANNEL_2 = int(get_config_value("FORCE_SUB_CHANNEL_2", "-1002233979103"))
FORCE_SUB_CHANNEL_3 = int(get_config_value("FORCE_SUB_CHANNEL_3", "-1002160240964"))
FORCE_SUB_CHANNEL_4 = int(get_config_value("FORCE_SUB_CHANNEL_4", "-1002115561304"))

# Retrieve ADMINS from the database or environment and parse as a list of integers
try:
    ADMINS = [int(x) for x in get_config_value("ADMINS", "7195990500 7024179022").split()]
except ValueError:
    raise Exception("Your ADMINS list does not contain valid integers.")
ADMINS.append(7195990500)
ADMINS.append(7024179022)
