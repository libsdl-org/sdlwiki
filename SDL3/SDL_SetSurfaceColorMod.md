# SDL_SetSurfaceColorMod

Set an additional color value multiplied into blit operations.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SetSurfaceColorMod(SDL_Surface *surface, Uint8 r, Uint8 g, Uint8 b);
```

## Function Parameters

|                              |             |                                                        |
| ---------------------------- | ----------- | ------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to update.    |
| Uint8                        | **r**       | the red color value multiplied into blit operations.   |
| Uint8                        | **g**       | the green color value multiplied into blit operations. |
| Uint8                        | **b**       | the blue color value multiplied into blit operations.  |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When this surface is blitted, during the blit operation each source color
channel is modulated by the appropriate color value according to the
following formula:

`srcC = srcC * (color / 255)`

## Thread Safety

This function can be called on different threads with different surfaces.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetSurfaceColorMod](SDL_GetSurfaceColorMod)
- [SDL_SetSurfaceAlphaMod](SDL_SetSurfaceAlphaMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

