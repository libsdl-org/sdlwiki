# SDL_DestroySurface

Free a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
void SDL_DestroySurface(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                         |
| ---------------------------- | ----------- | --------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) to free. |

## Remarks

It is safe to pass NULL to this function.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateSurface](SDL_CreateSurface)
- [SDL_CreateSurfaceFrom](SDL_CreateSurfaceFrom)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

