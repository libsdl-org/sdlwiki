# SDL_HINT_SHUTDOWN_DBUS_ON_QUIT

Cause SDL to call dbus_shutdown() on quit.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_SHUTDOWN_DBUS_ON_QUIT "SDL_SHUTDOWN_DBUS_ON_QUIT"
```

## Remarks

This is useful as a debug tool to validate memory leaks, but shouldn't ever
be set in production applications, as other libraries used by the
application might use dbus under the hood and this cause cause crashes if
they continue after [SDL_Quit](SDL_Quit)().

This variable can be set to the following values:

- "0": SDL will not call dbus_shutdown() on quit (default)
- "1": SDL will call dbus_shutdown() on quit

This hint is available since SDL 2.30.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

