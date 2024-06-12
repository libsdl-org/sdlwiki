###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyWindow

Destroy a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_DestroyWindow(SDL_Window * window);
```

## Function Parameters

|                            |            |                       |
| -------------------------- | ---------- | --------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to destroy |

## Remarks

If `window` is NULL, this function will return immediately after setting
the SDL error message to "Invalid window". See
[SDL_GetError](SDL_GetError)().

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateWindow](SDL_CreateWindow)
- [SDL_CreateWindowFrom](SDL_CreateWindowFrom)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

