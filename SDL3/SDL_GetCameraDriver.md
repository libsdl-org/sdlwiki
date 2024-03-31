###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCameraDriver

Use this function to get the name of a built in camera driver.

## Header File

Defined in [SDL_camera.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
const char* SDL_GetCameraDriver(int index);

```

## Function Parameters

|               |                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------- |
| **index**     | the index of the camera driver; the value ranges from 0 to [SDL_GetNumCameraDrivers](SDL_GetNumCameraDrivers)() - 1 |

## Return Value

Returns the name of the camera driver at the requested index, or NULL if an
invalid index was specified.

## Remarks

The list of camera drivers is given in the order that they are normally
initialized by default; the drivers that seem more reasonable to choose
first (as far as the SDL developers believe) are earlier in the list.

The names of drivers are all simple, low-ASCII identifiers, like "v4l2",
"coremedia" or "android". These never have Unicode characters, and are not
meant to be proper names.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumCameraDrivers](SDL_GetNumCameraDrivers)

----
[CategoryAPI](CategoryAPI)

