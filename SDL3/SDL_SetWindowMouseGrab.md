###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowMouseGrab

Set a window's mouse grab mode.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowMouseGrab(SDL_Window *window, bool grabbed);
```

## Function Parameters

|                            |             |                                                         |
| -------------------------- | ----------- | ------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**  | the window for which the mouse grab mode should be set. |
| bool                       | **grabbed** | this is true to grab mouse, and false to release.       |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Mouse grab confines the mouse cursor to the window.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetWindowMouseRect](SDL_GetWindowMouseRect)
- [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)
- [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse), [CategoryVideo](CategoryVideo)

