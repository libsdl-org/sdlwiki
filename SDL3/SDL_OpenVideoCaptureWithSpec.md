###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenVideoCaptureWithSpec

Open a Video Capture device and set specification 

## Syntax

```c
SDL_VideoCaptureDevice* SDL_OpenVideoCaptureWithSpec(SDL_VideoCaptureDeviceID instance_id,
                                                      const SDL_VideoCaptureSpec *desired,
                                                      SDL_VideoCaptureSpec *obtained,
                                                      int allowed_changes);

```

## Function Parameters

|                         |                                      |
| ----------------------- | ------------------------------------ |
| **instance_id**         | the video capture device instance ID |
| **desired**             | desired video capture spec           |
| **obtained**            | obtained video capture spec          |
| **allowed_changes**     | allow changes or not                 |

## Return Value

Returns device, or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenVideoCapture](SDL_OpenVideoCapture)
* [SDL_SetVideoCaptureSpec](SDL_SetVideoCaptureSpec)
* [SDL_GetVideoCaptureSpec](SDL_GetVideoCaptureSpec)

----
[CategoryAPI](CategoryAPI)

