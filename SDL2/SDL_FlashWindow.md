###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FlashWindow

Request a window to demand attention from the user.

## Syntax

```c
int SDL_FlashWindow(SDL_Window * window, SDL_FlashOperation operation);

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

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI.md)
