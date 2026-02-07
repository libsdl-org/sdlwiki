# SDL_CameraPermissionState

The current state of a request for camera access.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
typedef enum SDL_CameraPermissionState
{
    SDL_CAMERA_PERMISSION_STATE_DENIED = -1,
    SDL_CAMERA_PERMISSION_STATE_PENDING,
    SDL_CAMERA_PERMISSION_STATE_APPROVED
} SDL_CameraPermissionState;
```

## Version

This enum is available since SDL 3.4.0.

## See Also

- [SDL_GetCameraPermissionState](SDL_GetCameraPermissionState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryCamera](CategoryCamera)

