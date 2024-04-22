###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_ENABLE_SCREEN_KEYBOARD

A variable that controls whether the on-screen keyboard should be shown when text input is active

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ENABLE_SCREEN_KEYBOARD "SDL_ENABLE_SCREEN_KEYBOARD"
```

## Remarks

The variable can be set to the following values: "0" - Do not show the
on-screen keyboard "1" - Show the on-screen keyboard

The default value is "1". This hint must be set before text input is
activated.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

