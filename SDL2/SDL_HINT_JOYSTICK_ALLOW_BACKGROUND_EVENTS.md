###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS

A variable that lets you enable joystick (and gamecontroller) events even when your app is in the background.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS "SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"
```

## Remarks

The variable can be set to the following values:

- "0": Disable joystick & gamecontroller input events when the application
  is in the background.
- "1": Enable joystick & gamecontroller input events when the application
  is in the background.

The default value is "0". This hint may be set at any time.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)



