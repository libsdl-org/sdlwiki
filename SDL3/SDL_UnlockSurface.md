###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_UnlockSurface

Release a surface after directly accessing the pixels.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
void SDL_UnlockSurface(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                                          |
| ---------------------------- | ----------- | -------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to be unlocked. |

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_LockSurface](SDL_LockSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

