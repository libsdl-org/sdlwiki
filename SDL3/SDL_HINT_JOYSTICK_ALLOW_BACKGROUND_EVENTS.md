###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS

A variable that lets you enable joystick (and gamecontroller) events even when your app is in the background.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS "SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"
```

## Remarks

The variable can be set to the following values:

- "0": Disable joystick & gamecontroller input events when the application
  is in the background. (default)
- "1": Enable joystick & gamecontroller input events when the application
  is in the background.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

