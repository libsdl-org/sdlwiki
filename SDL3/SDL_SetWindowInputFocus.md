###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowInputFocus

Explicitly set input focus to the window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_SetWindowInputFocus(SDL_Window *window);

```

## Function Parameters

|                |                                            |
| -------------- | ------------------------------------------ |
| **window**     | the window that should get the input focus |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You almost certainly want [SDL_RaiseWindow](SDL_RaiseWindow)() instead of
this function. Use this with caution, as you might give focus to a window
that is completely obscured by other windows.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_RaiseWindow](SDL_RaiseWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

