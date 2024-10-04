###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetWindowSafeArea

Get the safe area for this window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GetWindowSafeArea(SDL_Window *window, SDL_Rect *rect);
```

## Function Parameters

|                            |            |                                                                                |
| -------------------------- | ---------- | ------------------------------------------------------------------------------ |
| [SDL_Window](SDL_Window) * | **window** | the window to query.                                                           |
| [SDL_Rect](SDL_Rect) *     | **rect**   | a pointer filled in with the client area that is safe for interactive content. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Some devices have portions of the screen which are partially obscured or
not interactive, possibly due to on-screen controls, curved edges, camera
notches, TV overscan, etc. This function provides the area of the window
which is safe to have interactible content. You should continue rendering
into the rest of the window, but it should not contain visually important
or interactible content.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

