###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowDisplayMode

Query the display mode to use when a window is visible at fullscreen.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GetWindowDisplayMode(SDL_Window * window,
                             SDL_DisplayMode * mode);

```

## Function Parameters

|                |                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------ |
| **window**     | the window to query                                                                        |
| **mode**       | an [SDL_DisplayMode](SDL_DisplayMode) structure filled in with the fullscreen display mode |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode)
- [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

