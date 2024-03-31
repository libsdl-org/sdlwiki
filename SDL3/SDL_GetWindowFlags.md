###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowFlags

Get the window flags.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_WindowFlags SDL_GetWindowFlags(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns a mask of the [SDL_WindowFlags](SDL_WindowFlags) associated with
`window`

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_HideWindow](SDL_HideWindow)
* [SDL_MaximizeWindow](SDL_MaximizeWindow)
* [SDL_MinimizeWindow](SDL_MinimizeWindow)
* [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)
* [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)
* [SDL_ShowWindow](SDL_ShowWindow)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


