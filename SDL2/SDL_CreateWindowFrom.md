###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateWindowFrom

Create an SDL window from an existing native window.

## Syntax

```c
SDL_Window * SDL_CreateWindowFrom(const void *data);

```

## Function Parameters

|              |                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------ |
| **data**     | a pointer to driver-dependent window creation data, typically your native window cast to a void* |

## Return Value

Returns the window that was created or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

In some cases (e.g. OpenGL) and on some platforms (e.g. Microsoft Windows)
the hint
[`SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT`](SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT)
needs to be configured before using
[SDL_CreateWindowFrom](SDL_CreateWindowFrom.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow.md)
* [SDL_DestroyWindow](SDL_DestroyWindow.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
