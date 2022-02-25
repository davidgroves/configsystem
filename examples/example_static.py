import configurator

static_config = configurator.Static(name="basic_static_config", register=True)
static_config.set("Sky", "Blue")
static_config.set("Grass", "Green")

assert configurator.ConfigRegistry.get_item("basic_static_config", "Sky") == "Blue"
