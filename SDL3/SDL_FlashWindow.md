###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FlashWindow

Request a window to demand attention from the user.

## Syntax

```c
int SDL_FlashWindow(SDL_Window *window, SDL_FlashOperation operation);

```

## Function Parameters

|                   |                          |
| ----------------- | ------------------------ |
| **window**        | the window to be flashed |
| **operation**     | the flash operation      |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Structures

:[https://wiki.libsdl.org/SDL_FlashOperation SDL_FlashOperation]

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
