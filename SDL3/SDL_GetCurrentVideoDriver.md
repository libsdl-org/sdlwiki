###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentVideoDriver

Get the name of the currently initialized video driver.

## Syntax

```c
const char* SDL_GetCurrentVideoDriver(void);

```

## Return Value

Returns the name of the current video driver or NULL if no driver has been
initialized.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers.md)
* [SDL_GetVideoDriver](SDL_GetVideoDriver.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
