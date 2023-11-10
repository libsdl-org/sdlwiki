###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AcquireVideoCaptureFrame

Acquire a frame.

## Syntax

```c
int SDL_AcquireVideoCaptureFrame(SDL_VideoCaptureDevice *device, SDL_VideoCaptureFrame *frame);

```

## Function Parameters

|                |                             |
| -------------- | --------------------------- |
| **device**     | opened video capture device |
| **frame**      | pointer to get the frame    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The frame is a memory pointer to the image data, whose size and format are
given by the the obtained spec.

Non blocking API. If there is a frame available, frame->num_planes is non
0. If frame->num_planes is 0 and returned code is 0, there is no frame at
that time.

After used, the frame should be released with
[SDL_ReleaseVideoCaptureFrame](SDL_ReleaseVideoCaptureFrame)

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_ReleaseVideoCaptureFrame](SDL_ReleaseVideoCaptureFrame)

----
[CategoryAPI](CategoryAPI)

