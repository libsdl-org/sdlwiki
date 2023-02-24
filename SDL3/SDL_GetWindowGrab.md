###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowGrab

Get a window's input grab mode.

## Syntax

```c
SDL_bool SDL_GetWindowGrab(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if input is grabbed, [SDL_FALSE](SDL_FALSE)
otherwise.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowGrab](SDL_SetWindowGrab)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


