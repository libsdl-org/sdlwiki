# SDL_HINT_JOYSTICK_HIDAPI_COMBINE_JOY_CONS

A variable controlling whether Nintendo Switch Joy-Con controllers will be combined into a single Pro-like controller when using the HIDAPI driver.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_COMBINE_JOY_CONS "SDL_JOYSTICK_HIDAPI_COMBINE_JOY_CONS"
```

## Remarks

The variable can be set to the following values:

- "0": Left and right Joy-Con controllers will not be combined and each
  will be a mini-gamepad.
- "1": Left and right Joy-Con controllers will be combined into a single
  controller. (default)

This hint should be set before initializing joysticks and gamepads.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

