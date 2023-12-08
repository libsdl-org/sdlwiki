###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowMouseRect

Confines the cursor to the specified area of a window.

## Syntax

```c
int SDL_SetWindowMouseRect(SDL_Window * window, const SDL_Rect * rect);

```

## Function Parameters

|                |                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------- |
| **window**     | The window that will be associated with the barrier.                                                             |
| **rect**       | A rectangle area in window-relative coordinates. If NULL the barrier for the specified window will be destroyed. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Note that this does NOT grab the cursor, it only defines the area a cursor
is restricted to when the window has mouse focus.

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_GetWindowMouseRect](SDL_GetWindowMouseRect.md)
* [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab.md)

----
[CategoryAPI](CategoryAPI.md)
