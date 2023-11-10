###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVideoCaptureDevices

Get a list of currently connected video capture devices.

## Syntax

```c
SDL_VideoCaptureDeviceID* SDL_GetVideoCaptureDevices(int *count);

```

## Function Parameters

|               |                                                              |
| ------------- | ------------------------------------------------------------ |
| **count**     | a pointer filled in with the number of video capture devices |

## Return Value

Returns a 0 terminated array of video capture instance IDs which should be
freed with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenVideoCapture](SDL_OpenVideoCapture)

----
[CategoryAPI](CategoryAPI)

