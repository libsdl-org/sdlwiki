###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetCurrentVideoDriver

Get the name of the currently initialized video driver.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
const char* SDL_GetCurrentVideoDriver(void);

```

## Return Value

Returns the name of the current video driver or NULL if no driver has been
initialized.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)
- [SDL_GetVideoDriver](SDL_GetVideoDriver)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

