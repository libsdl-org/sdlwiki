###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_MAC_BACKGROUND_APP

A variable controlling whether to force the application to become the foreground process when launched on macOS.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MAC_BACKGROUND_APP "SDL_MAC_BACKGROUND_APP"
```

## Remarks

The variable can be set to the following values:

- "0": The application is brought to the foreground when launched.
  (default)
- "1": The application may remain in the background when launched.

This hint needs to be set before [SDL_Init](SDL_Init)().

## Version

This hint is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

