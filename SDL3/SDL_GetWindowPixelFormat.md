# SDL_GetWindowPixelFormat

Get the pixel format associated with the window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_PixelFormat SDL_GetWindowPixelFormat(SDL_Window *window);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query. |

## Return Value

([SDL_PixelFormat](SDL_PixelFormat)) Returns the pixel format of the window
on success or [SDL_PIXELFORMAT_UNKNOWN](SDL_PIXELFORMAT_UNKNOWN) on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

