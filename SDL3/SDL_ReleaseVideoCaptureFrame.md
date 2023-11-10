###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReleaseVideoCaptureFrame

Release a frame.

## Syntax

```c
int SDL_ReleaseVideoCaptureFrame(SDL_VideoCaptureDevice *device, SDL_VideoCaptureFrame *frame);

```

## Function Parameters

|                |                             |
| -------------- | --------------------------- |
| **device**     | opened video capture device |
| **frame**      | frame pointer.              |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Let the back-end re-use the internal buffer for video capture.

All acquired frames should be released before closing the device.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AcquireVideoCaptureFrame](SDL_AcquireVideoCaptureFrame)

----
[CategoryAPI](CategoryAPI)

