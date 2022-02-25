import os

from configurator import ConfigRegistry
from config_types import JsonConfig

# Set the sky to daytime.
os.unlink("files/sky_current.json")
os.symlink("sky_day.json", "files/sky_current.json")

# Load the config
json_config = JsonConfig(name="sky", register=True, source="files/sky_current.json", dynamic_reload=True)

# Show the sky is blue in the day
sky_colour = ConfigRegistry.get_item("sky", "colour")
print(f"The sky during the day is {sky_colour}")

# Change the file to night
os.unlink("files/sky_current.json")
os.symlink("sky_night.json", "files/sky_current.json")

# Reload configs.
# This is done on receipt of a SIGHUP on POSIX systems.
ConfigRegistry.refresh_all()

# Show the sky is black at night
sky_colour = ConfigRegistry.get_item("sky", "colour")
print(f"The sky during the night is {sky_colour}")
