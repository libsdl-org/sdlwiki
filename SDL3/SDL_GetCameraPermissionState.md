# SDL_GetCameraPermissionState

Query if camera access has been approved by the user.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
SDL_CameraPermissionState SDL_GetCameraPermissionState(SDL_Camera *camera);
```

## Function Parameters

|                            |            |                                    |
| -------------------------- | ---------- | ---------------------------------- |
| [SDL_Camera](SDL_Camera) * | **camera** | the opened camera device to query. |

## Return Value

([SDL_CameraPermissionState](SDL_CameraPermissionState)) Returns an
[SDL_CameraPermissionState](SDL_CameraPermissionState) value indicating if
access is granted, or
[`SDL_CAMERA_PERMISSION_STATE_PENDING`](SDL_CAMERA_PERMISSION_STATE_PENDING)
if the decision is still pending.

## Remarks

Cameras will not function between when the device is opened by the app and
when the user permits access to the hardware. On some platforms, this
presents as a popup dialog where the user has to explicitly approve access;
on others the approval might be implicit and not alert the user at all.

This function can be used to check the status of that approval. It will
return
[SDL_CAMERA_PERMISSION_STATE_PENDING](SDL_CAMERA_PERMISSION_STATE_PENDING)
if waiting for user response,
[SDL_CAMERA_PERMISSION_STATE_APPROVED](SDL_CAMERA_PERMISSION_STATE_APPROVED)
if the camera is approved for use, and
[SDL_CAMERA_PERMISSION_STATE_DENIED](SDL_CAMERA_PERMISSION_STATE_DENIED) if
the user denied access.

Instead of polling with this function, you can wait for a
[SDL_EVENT_CAMERA_DEVICE_APPROVED](SDL_EVENT_CAMERA_DEVICE_APPROVED) (or
[SDL_EVENT_CAMERA_DEVICE_DENIED](SDL_EVENT_CAMERA_DEVICE_DENIED)) event in
the standard SDL event loop, which is guaranteed to be sent once when
permission to use the camera is decided.

If a camera is declined, there's nothing to be done but call
[SDL_CloseCamera](SDL_CloseCamera)() to dispose of it.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_OpenCamera](SDL_OpenCamera)
- [SDL_CloseCamera](SDL_CloseCamera)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

