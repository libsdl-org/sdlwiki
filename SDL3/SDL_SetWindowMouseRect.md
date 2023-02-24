###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowMouseRect

Confines the cursor to the specified area of a window.

## Syntax

```c
int SDL_SetWindowMouseRect(SDL_Window *window, const SDL_Rect *rect);

```

## Function Parameters

|                |                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------- |
| **window**     | The window that will be associated with the barrier.                                                             |
| **rect**       | A rectangle area in window-relative coordinates. If NULL the barrier for the specified window will be destroyed. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Note that this does NOT grab the cursor, it only defines the area a cursor
is restricted to when the window has mouse focus.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowMouseRect](SDL_GetWindowMouseRect)
* [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)

----
[CategoryAPI](CategoryAPI)

