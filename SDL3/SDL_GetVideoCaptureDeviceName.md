###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVideoCaptureDeviceName

Get device name 

## Syntax

```c
const char * SDL_GetVideoCaptureDeviceName(SDL_VideoCaptureDeviceID instance_id);

```

## Function Parameters

|                     |                                      |
| ------------------- | ------------------------------------ |
| **instance_id**     | the video capture device instance ID |

## Return Value

Returns device name, shouldn't be freed

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetVideoCaptureDevices](SDL_GetVideoCaptureDevices)

----
[CategoryAPI](CategoryAPI)

