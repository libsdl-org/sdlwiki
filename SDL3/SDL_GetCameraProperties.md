###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCameraProperties

Get the properties associated with an opened camera.

## Header File

Defined in [SDL_camera.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_PropertiesID SDL_GetCameraProperties(SDL_Camera *camera);

```

## Function Parameters

|                |                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------- |
| **camera**     | the [SDL_Camera](SDL_Camera) obtained from [SDL_OpenCameraDevice](SDL_OpenCameraDevice)() |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

