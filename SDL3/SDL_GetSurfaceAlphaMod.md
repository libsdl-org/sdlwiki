# SDL_GetSurfaceAlphaMod

Get the additional alpha value used in blit operations.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_GetSurfaceAlphaMod(SDL_Surface *surface, Uint8 *alpha);
```

## Function Parameters

|                              |             |                                                    |
| ---------------------------- | ----------- | -------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to query. |
| Uint8 *                      | **alpha**   | a pointer filled in with the current alpha value.  |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetSurfaceColorMod](SDL_GetSurfaceColorMod)
- [SDL_SetSurfaceAlphaMod](SDL_SetSurfaceAlphaMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

