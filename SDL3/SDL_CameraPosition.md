###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CameraPosition

The position of camera in relation to system device.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
typedef enum SDL_CameraPosition
{
    SDL_CAMERA_POSITION_UNKNOWN,
    SDL_CAMERA_POSITION_FRONT_FACING,
    SDL_CAMERA_POSITION_BACK_FACING
} SDL_CameraPosition;
```

## Version

This enum is available since SDL 3.0.0.

## See Also

- [SDL_GetCameraDevicePosition](SDL_GetCameraDevicePosition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

