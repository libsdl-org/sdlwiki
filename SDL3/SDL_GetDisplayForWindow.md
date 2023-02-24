###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDisplayForWindow

Get the display associated with a window.

## Syntax

```c
SDL_DisplayID SDL_GetDisplayForWindow(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the instance ID of the display containing the center of the window
on success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetDisplayBounds](SDL_GetDisplayBounds)
* [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI)

