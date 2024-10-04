###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ClearSurface

Clear a surface with a specific color, with floating point precision.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_ClearSurface(SDL_Surface *surface, float r, float g, float b, float a);
```

## Function Parameters

|                              |             |                                                              |
| ---------------------------- | ----------- | ------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) to clear.                     |
| float                        | **r**       | the red component of the pixel, normally in the range 0-1.   |
| float                        | **g**       | the green component of the pixel, normally in the range 0-1. |
| float                        | **b**       | the blue component of the pixel, normally in the range 0-1.  |
| float                        | **a**       | the alpha component of the pixel, normally in the range 0-1. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function handles all surface formats, and ignores any clip rectangle.

If the surface is YUV, the color is assumed to be in the sRGB colorspace,
otherwise the color is assumed to be in the colorspace of the suface.

## Version

This function is available since SDL 3.0.0.

## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

