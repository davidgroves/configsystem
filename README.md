Configurator
============

A generic configuration handling system.

Supports config from :-
- Static (you need to write Python code for this)
- Json
- Yaml
- Environment Variables

Designed to specifically support dynamic configuration reloading, via sending the POSIX HUP signal.
Support for this on Windows doesn't exist.

```bash
# Ask for all Dynamic Configs to be reloaded.
$ kill -HUP $PID
```

Examples
========

See the example files in the ```examples/``` directory.

Wishlist
========

Add .ini and .toml file support.

Bugs
====

No dynamic reload support on windows.