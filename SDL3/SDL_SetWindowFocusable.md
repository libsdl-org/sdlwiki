###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowFocusable

Set whether the window may have input focus.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowFocusable(SDL_Window *window, bool focusable);
```

## Function Parameters

|                            |               |                                                            |
| -------------------------- | ------------- | ---------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**    | the window to set focusable state.                         |
| bool                       | **focusable** | true to allow input focus, false to not allow input focus. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

