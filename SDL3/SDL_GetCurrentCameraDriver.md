###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentCameraDriver

Get the name of the current camera driver.

## Header File

Defined in [SDL_camera.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
const char* SDL_GetCurrentCameraDriver(void);

```

## Return Value

Returns the name of the current camera driver or NULL if no driver has been
initialized.

## Remarks

The returned string points to internal static memory and thus never becomes
invalid, even if you quit the camera subsystem and initialize a new driver
(although such a case would return a different static string from another
call to this function, of course). As such, you should not modify or free
the returned string.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

