###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCameraDeviceName

Get the human-readable device name for a camera.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
const char * SDL_GetCameraDeviceName(SDL_CameraDeviceID instance_id);
```

## Function Parameters

|                                          |                 |                                |
| ---------------------------------------- | --------------- | ------------------------------ |
| [SDL_CameraDeviceID](SDL_CameraDeviceID) | **instance_id** | the camera device instance ID. |

## Return Value

(const char *) Returns a human-readable device name, or NULL on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetCameraDevices](SDL_GetCameraDevices)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

