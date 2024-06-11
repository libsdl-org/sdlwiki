###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentVideoDriver

Get the name of the currently initialized video driver.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const char* SDL_GetCurrentVideoDriver(void);
```

## Return Value

Returns the name of the current video driver or NULL if no driver has been
initialized.

## Remarks

The names of drivers are all simple, low-ASCII identifiers, like "cocoa",
"x11" or "windows". These never have Unicode characters, and are not meant
to be proper names.

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)
- [SDL_GetVideoDriver](SDL_GetVideoDriver)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

