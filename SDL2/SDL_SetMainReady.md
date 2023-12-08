###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetMainReady

Circumvent failure of [SDL_Init](SDL_Init.md)() when not using [SDL_main](SDL_main.md)() as an entry point.

## Syntax

```c
void SDL_SetMainReady(void);

```

## Remarks

This function is defined in [SDL_main](SDL_main.md).h, along with the
preprocessor rule to redefine main() as [SDL_main](SDL_main.md)(). Thus to
ensure that your main() function will not be changed it is necessary to
define [SDL_MAIN_HANDLED](SDL_MAIN_HANDLED.md) before including SDL.h.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_Init](SDL_Init.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryInit](CategoryInit.md)
