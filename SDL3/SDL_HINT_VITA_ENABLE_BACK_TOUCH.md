###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_VITA_ENABLE_BACK_TOUCH

A variable controlling whether touch should be enabled on the back panel of the PlayStation Vita.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VITA_ENABLE_BACK_TOUCH "SDL_VITA_ENABLE_BACK_TOUCH"
```

## Remarks

The variable can be set to the following values:

- "0": Disable touch on the back panel.
- "1": Enable touch on the back panel. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

