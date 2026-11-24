# SDL_SetWindowMousePassthrough

Enable or disable mouse passthrough for a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowMousePassthrough(SDL_Window *window, bool passthrough);
```

## Function Parameters

|                            |                 |                                                                                  |
| -------------------------- | --------------- | -------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**      | the window to set mouse passthrough for.                                         |
| bool                       | **passthrough** | true to make the window transparent to mouse input, false to accept mouse input. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_MOUSE_PASSTHROUGH`](SDL_WINDOW_MOUSE_PASSTHROUGH) flag.

When enabled, the window will lose mouse focus and will not get any further
mouse events (except button up events for buttons held down at the time)
and clicks in the window will go through and hit windows behind it.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

