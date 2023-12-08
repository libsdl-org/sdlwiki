###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumVideoDrivers

Get the number of video drivers compiled into SDL.

## Syntax

```c
int SDL_GetNumVideoDrivers(void);

```

## Return Value

Returns a number >= 1 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetVideoDriver](SDL_GetVideoDriver.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
