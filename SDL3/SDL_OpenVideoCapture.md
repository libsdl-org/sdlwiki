###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenVideoCapture

Open a Video Capture device 

## Syntax

```c
SDL_VideoCaptureDevice* SDL_OpenVideoCapture(SDL_VideoCaptureDeviceID instance_id);

```

## Function Parameters

|                     |                                      |
| ------------------- | ------------------------------------ |
| **instance_id**     | the video capture device instance ID |

## Return Value

Returns device, or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetVideoCaptureDeviceName](SDL_GetVideoCaptureDeviceName)
* [SDL_GetVideoCaptureDevices](SDL_GetVideoCaptureDevices)
* [SDL_OpenVideoCaptureWithSpec](SDL_OpenVideoCaptureWithSpec)

----
[CategoryAPI](CategoryAPI)

