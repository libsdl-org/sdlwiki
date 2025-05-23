# SDL_GetWindowMouseRect

Get the mouse confinement rectangle of a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const SDL_Rect * SDL_GetWindowMouseRect(SDL_Window *window);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query. |

## Return Value

(const [SDL_Rect](SDL_Rect) *) Returns a pointer to the mouse confinement
rectangle of a window, or NULL if there isn't one.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetWindowMouseRect](SDL_SetWindowMouseRect)
- [SDL_GetWindowMouseGrab](SDL_GetWindowMouseGrab)
- [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo), [CategoryMouse](CategoryMouse), 


