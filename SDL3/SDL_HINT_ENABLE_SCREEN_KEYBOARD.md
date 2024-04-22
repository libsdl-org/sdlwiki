###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_ENABLE_SCREEN_KEYBOARD

A variable that controls whether the on-screen keyboard should be shown when text input is active.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ENABLE_SCREEN_KEYBOARD "SDL_ENABLE_SCREEN_KEYBOARD"
```

## Remarks

The variable can be set to the following values:

- "auto": The on-screen keyboard will be shown if there is no physical
  keyboard attached. (default)
- "0": Do not show the on-screen keyboard.
- "1": Show the on-screen keyboard, if available.

This hint must be set before [SDL_StartTextInput](SDL_StartTextInput)() is
called

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

