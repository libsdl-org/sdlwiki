###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowFlags

Get the window flags.

## Syntax

```c
Uint32 SDL_GetWindowFlags(SDL_Window * window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns a mask of the [SDL_WindowFlags](SDL_WindowFlags.md) associated with
`window`

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow.md)
* [SDL_HideWindow](SDL_HideWindow.md)
* [SDL_MaximizeWindow](SDL_MaximizeWindow.md)
* [SDL_MinimizeWindow](SDL_MinimizeWindow.md)
* [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen.md)
* [SDL_SetWindowGrab](SDL_SetWindowGrab.md)
* [SDL_ShowWindow](SDL_ShowWindow.md)

----
[CategoryAPI](CategoryAPI.md)
