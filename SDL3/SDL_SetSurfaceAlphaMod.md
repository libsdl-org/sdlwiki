###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetSurfaceAlphaMod

Set an additional alpha value used in blit operations.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SetSurfaceAlphaMod(SDL_Surface *surface, Uint8 alpha);
```

## Function Parameters

|                              |             |                                                     |
| ---------------------------- | ----------- | --------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to update. |
| Uint8                        | **alpha**   | the alpha value multiplied into blit operations.    |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When this surface is blitted, during the blit operation the source alpha
value is modulated by this alpha value according to the following formula:

`srcA = srcA * (alpha / 255)`

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetSurfaceAlphaMod](SDL_GetSurfaceAlphaMod)
- [SDL_SetSurfaceColorMod](SDL_SetSurfaceColorMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

