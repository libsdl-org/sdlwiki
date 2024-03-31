###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetYUVConversionModeForResolution

Get the YUV conversion mode, returning the correct mode for the resolution when the current conversion mode is [SDL_YUV_CONVERSION_AUTOMATIC](SDL_YUV_CONVERSION_AUTOMATIC) 

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_YUV_CONVERSION_MODE SDL_GetYUVConversionModeForResolution(int width, int height);

```

## Version

This function is available since SDL 2.0.8.

----
[CategoryAPI](CategoryAPI)

