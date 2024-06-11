###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentCameraDriver

Get the name of the current camera driver.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
const char* SDL_GetCurrentCameraDriver(void);
```

## Return Value

Returns the name of the current camera driver or NULL if no driver has been
initialized.

## Remarks

The names of drivers are all simple, low-ASCII identifiers, like "v4l2",
"coremedia" or "android". These never have Unicode characters, and are not
meant to be proper names.

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

