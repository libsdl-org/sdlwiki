# SDL_SetWindowMousePassthrough

Enable or disable mouse passthrough for a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowMousePassthrough(SDL_Window *window, bool passthrough);
```

## Function Parameters

|                            |                 |                                                                                   |
| -------------------------- | --------------- | --------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**      | the window to set mouse passthrough for.                                          |
| bool                       | **passthrough** | true to make the window transparent to mouse input, false to capture mouse input. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

