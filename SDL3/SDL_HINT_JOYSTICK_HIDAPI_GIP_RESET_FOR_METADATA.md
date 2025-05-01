# SDL_HINT_JOYSTICK_HIDAPI_GIP_RESET_FOR_METADATA

A variable controlling whether the new HIDAPI driver for wired Xbox One (GIP) controllers should reset the controller if it can't get the metadata from the controller.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_GIP_RESET_FOR_METADATA "SDL_JOYSTICK_HIDAPI_GIP_RESET_FOR_METADATA"
```

## Remarks

The variable can be set to the following values:

- "0": Assume this is a generic controller.
- "1": Reset the controller to get metadata.

By default the controller is not reset.

This hint should be set before initializing joysticks and gamepads.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

