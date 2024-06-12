###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCameraPermissionState

Query if camera access has been approved by the user.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
int SDL_GetCameraPermissionState(SDL_Camera *camera);
```

## Function Parameters

|                            |            |                                   |
| -------------------------- | ---------- | --------------------------------- |
| [SDL_Camera](SDL_Camera) * | **camera** | the opened camera device to query |

## Return Value

(int) Returns -1 if user denied access to the camera, 1 if user approved
access, 0 if no decision has been made yet.

## Remarks

Cameras will not function between when the device is opened by the app and
when the user permits access to the hardware. On some platforms, this
presents as a popup dialog where the user has to explicitly approve access;
on others the approval might be implicit and not alert the user at all.

This function can be used to check the status of that approval. It will
return 0 if still waiting for user response, 1 if the camera is approved
for use, and -1 if the user denied access.

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

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenCameraDevice](SDL_OpenCameraDevice)
- [SDL_CloseCamera](SDL_CloseCamera)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

