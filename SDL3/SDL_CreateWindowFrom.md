###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateWindowFrom

Create an SDL window from an existing native window.

## Syntax

```c
SDL_Window* SDL_CreateWindowFrom(const void *data);

```

## Function Parameters

|              |                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------ |
| **data**     | a pointer to driver-dependent window creation data, typically your native window cast to a void* |

## Return Value

Returns the window that was created or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

In some cases (e.g. OpenGL) and on some platforms (e.g. Microsoft Windows)
the hint
[`SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT`](SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT)
needs to be configured before using
[SDL_CreateWindowFrom](SDL_CreateWindowFrom)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


