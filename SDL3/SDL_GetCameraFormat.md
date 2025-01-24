# SDL_GetCameraFormat

Get the spec that a camera is using when generating images.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
bool SDL_GetCameraFormat(SDL_Camera *camera, SDL_CameraSpec *spec);
```

## Function Parameters

|                                    |            |                                                                          |
| ---------------------------------- | ---------- | ------------------------------------------------------------------------ |
| [SDL_Camera](SDL_Camera) *         | **camera** | opened camera device.                                                    |
| [SDL_CameraSpec](SDL_CameraSpec) * | **spec**   | the [SDL_CameraSpec](SDL_CameraSpec) to be initialized by this function. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Note that this might not be the native format of the hardware, as SDL might
be converting to this format behind the scenes.

If the system is waiting for the user to approve access to the camera, as
some platforms require, this will return false, but this isn't necessarily
a fatal error; you should either wait for an
[SDL_EVENT_CAMERA_DEVICE_APPROVED](SDL_EVENT_CAMERA_DEVICE_APPROVED) (or
[SDL_EVENT_CAMERA_DEVICE_DENIED](SDL_EVENT_CAMERA_DEVICE_DENIED)) event, or
poll [SDL_GetCameraPermissionState](SDL_GetCameraPermissionState)()
occasionally until it returns non-zero.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_OpenCamera](SDL_OpenCamera)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

