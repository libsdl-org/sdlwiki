###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCameraDevicePosition

Get the position of the camera in relation to the system.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
SDL_CameraPosition SDL_GetCameraDevicePosition(SDL_CameraDeviceID instance_id);
```

## Function Parameters

|                                          |                 |                               |
| ---------------------------------------- | --------------- | ----------------------------- |
| [SDL_CameraDeviceID](SDL_CameraDeviceID) | **instance_id** | the camera device instance ID |

## Return Value

([SDL_CameraPosition](SDL_CameraPosition)) Returns the position of the
camera on the system hardware.

## Remarks

Most platforms will report UNKNOWN, but mobile devices, like phones, can
often make a distiction between cameras on the front of the device (that
points towards the user, for taking "selfies") and cameras on the back (for
filming in the direction the user is facing).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetCameraDevices](SDL_GetCameraDevices)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

