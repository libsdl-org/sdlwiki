###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetWindowMouseGrab

Get a window's mouse grab mode.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GetWindowMouseGrab(SDL_Window *window);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query. |

## Return Value

(bool) Returns true if mouse is grabbed, and false otherwise.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetWindowMouseRect](SDL_GetWindowMouseRect)
- [SDL_SetWindowMouseRect](SDL_SetWindowMouseRect)
- [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)
- [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse), [CategoryVideo](CategoryVideo)

