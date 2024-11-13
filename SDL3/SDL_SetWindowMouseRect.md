###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowMouseRect

Confines the cursor to the specified area of a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowMouseRect(SDL_Window *window, const SDL_Rect *rect);
```

## Function Parameters

|                              |            |                                                                                                                  |
| ---------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) *   | **window** | the window that will be associated with the barrier.                                                             |
| const [SDL_Rect](SDL_Rect) * | **rect**   | a rectangle area in window-relative coordinates. If NULL the barrier for the specified window will be destroyed. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Note that this does NOT grab the cursor, it only defines the area a cursor
is restricted to when the window has mouse focus.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetWindowMouseRect](SDL_GetWindowMouseRect)
- [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse), [CategoryVideo](CategoryVideo)

