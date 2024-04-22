###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_FILE_DIALOG_DRIVER

A variable that specifies a dialog backend to use.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_FILE_DIALOG_DRIVER "SDL_FILE_DIALOG_DRIVER"
```

## Remarks

By default, SDL will try all available dialog backends in a reasonable
order until it finds one that can work, but this hint allows the app or
user to force a specific target.

If the specified target does not exist or is not available, the
dialog-related function calls will fail.

This hint currently only applies to platforms using the generic "Unix"
dialog implementation, but may be extended to more platforms in the future.
Note that some Unix and Unix-like platforms have their own implementation,
such as macOS and Haiku.

The variable can be set to the following values:

- NULL: Select automatically (default, all platforms)
- "portal": Use XDG Portals through DBus (Unix only)
- "zenity": Use the Zenity program (Unix only)

More options may be added in the future.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

