###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentVideoDriver

Get the name of the currently initialized video driver.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const char* SDL_GetCurrentVideoDriver(void);

```

## Return Value

Returns the name of the current video driver or NULL if no driver has been
initialized.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)
* [SDL_GetVideoDriver](SDL_GetVideoDriver)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)


