###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumCameraDrivers

Use this function to get the number of built-in camera drivers.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
int SDL_GetNumCameraDrivers(void);

```

## Return Value

Returns the number of built-in camera drivers.

## Remarks

This function returns a hardcoded number. This never returns a negative
value; if there are no drivers compiled into this build of SDL, this
function returns zero. The presence of a driver in this list does not mean
it will function, it just means SDL is capable of interacting with that
interface. For example, a build of SDL might have v4l2 support, but if
there's no kernel support available, SDL's v4l2 driver would fail if used.

By default, SDL tries all drivers, in its preferred order, until one is
found to be usable.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetCameraDriver](SDL_GetCameraDriver)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

