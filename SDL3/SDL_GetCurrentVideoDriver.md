# SDL_GetCurrentVideoDriver

Get the name of the currently initialized video driver.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const char * SDL_GetCurrentVideoDriver(void);
```

## Return Value

(const char *) Returns the name of the current video driver or NULL if no
driver has been initialized.

## Remarks

The names of drivers are all simple, low-ASCII identifiers, like "cocoa",
"x11" or "windows". These never have Unicode characters, and are not meant
to be proper names.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)
- [SDL_GetVideoDriver](SDL_GetVideoDriver)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

