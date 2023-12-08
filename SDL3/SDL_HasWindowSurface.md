###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasWindowSurface

Return whether the window has a surface associated with it.

## Syntax

```c
SDL_bool SDL_HasWindowSurface(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if there is a surface associated with the
window, or [SDL_FALSE](SDL_FALSE.md) otherwise.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowSurface](SDL_GetWindowSurface.md)

----
[CategoryAPI](CategoryAPI.md)
