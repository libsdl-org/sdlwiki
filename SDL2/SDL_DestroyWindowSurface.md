###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyWindowSurface

Destroy the surface associated with the window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_DestroyWindowSurface(SDL_Window *window);
```

## Function Parameters

|                            |            |                       |
| -------------------------- | ---------- | --------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to update. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.28.0.

## See Also

- [SDL_GetWindowSurface](SDL_GetWindowSurface)
- [SDL_HasWindowSurface](SDL_HasWindowSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

