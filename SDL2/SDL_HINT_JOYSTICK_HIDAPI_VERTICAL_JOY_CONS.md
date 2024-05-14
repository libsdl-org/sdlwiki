###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_HIDAPI_VERTICAL_JOY_CONS

A variable controlling whether Nintendo Switch Joy-Con controllers will be in vertical mode when using the HIDAPI driver

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_VERTICAL_JOY_CONS "SDL_JOYSTICK_HIDAPI_VERTICAL_JOY_CONS"
```

## Remarks

This variable can be set to the following values:

- "0": Left and right Joy-Con controllers will not be in vertical mode (the
  default)
- "1": Left and right Joy-Con controllers will be in vertical mode

This hint must be set before calling
[SDL_Init](SDL_Init)([SDL_INIT_GAMECONTROLLER](SDL_INIT_GAMECONTROLLER))

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

