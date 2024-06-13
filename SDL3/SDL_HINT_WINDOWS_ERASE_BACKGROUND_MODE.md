###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINDOWS_ERASE_BACKGROUND_MODE

A variable controlling whether SDL will clear the window contents when the WM_ERASEBKGND message is received.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_ERASE_BACKGROUND_MODE "SDL_WINDOWS_ERASE_BACKGROUND_MODE"
```

## Remarks

The variable can be set to the following values:

- "0"/"never": Never clear the window.
- "1"/"initial": Clear the window when the first WM_ERASEBKGND event fires.
  (default)
- "2"/"always": Clear the window on every WM_ERASEBKGND event.

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

