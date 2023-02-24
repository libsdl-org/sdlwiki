###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)
* [SDL_GetVideoDriver](SDL_GetVideoDriver)

----
[CategoryAPI](CategoryAPI)

