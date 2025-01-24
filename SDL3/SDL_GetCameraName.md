# SDL_GetCameraName

Get the human-readable device name for a camera.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
const char * SDL_GetCameraName(SDL_CameraID instance_id);
```

## Function Parameters

|                              |                 |                                |
| ---------------------------- | --------------- | ------------------------------ |
| [SDL_CameraID](SDL_CameraID) | **instance_id** | the camera device instance ID. |

## Return Value

(const char *) Returns a human-readable device name or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetCameras](SDL_GetCameras)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

