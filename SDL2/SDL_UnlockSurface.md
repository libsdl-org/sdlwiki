# SDL_UnlockSurface

Release a surface after directly accessing the pixels.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
void SDL_UnlockSurface(SDL_Surface * surface);
```

## Function Parameters

|                              |             |                                                          |
| ---------------------------- | ----------- | -------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to be unlocked. |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_LockSurface](SDL_LockSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

