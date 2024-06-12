###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCameraInstanceID

Get the instance ID of an opened camera.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
SDL_CameraDeviceID SDL_GetCameraInstanceID(SDL_Camera *camera);
```

## Function Parameters

|                            |            |                                      |
| -------------------------- | ---------- | ------------------------------------ |
| [SDL_Camera](SDL_Camera) * | **camera** | an [SDL_Camera](SDL_Camera) to query |

## Return Value

([SDL_CameraDeviceID](SDL_CameraDeviceID)) Returns the instance ID of the
specified camera on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenCameraDevice](SDL_OpenCameraDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

