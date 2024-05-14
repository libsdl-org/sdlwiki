###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_SHUTDOWN_DBUS_ON_QUIT

A variable controlling whether SDL calls dbus_shutdown() on quit.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_SHUTDOWN_DBUS_ON_QUIT "SDL_SHUTDOWN_DBUS_ON_QUIT"
```

## Remarks

This is useful as a debug tool to validate memory leaks, but shouldn't ever
be set in production applications, as other libraries used by the
application might use dbus under the hood and this cause cause crashes if
they continue after [SDL_Quit](SDL_Quit)().

The variable can be set to the following values:

- "0": SDL will not call dbus_shutdown() on quit. (default)
- "1": SDL will call dbus_shutdown() on quit.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

