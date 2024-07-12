###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCameraProperties

Get the properties associated with an opened camera.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
SDL_PropertiesID SDL_GetCameraProperties(SDL_Camera *camera);
```

## Function Parameters

|                            |            |                                                                                            |
| -------------------------- | ---------- | ------------------------------------------------------------------------------------------ |
| [SDL_Camera](SDL_Camera) * | **camera** | the [SDL_Camera](SDL_Camera) obtained from [SDL_OpenCameraDevice](SDL_OpenCameraDevice)(). |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

