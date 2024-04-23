###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AcquireCameraFrame

Acquire a frame.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
SDL_Surface * SDL_AcquireCameraFrame(SDL_Camera *camera, Uint64 *timestampNS);

```

## Function Parameters

|                     |                                                                             |
| ------------------- | --------------------------------------------------------------------------- |
| **camera**          | opened camera device                                                        |
| **timestampNS**     | a pointer filled in with the frame's timestamp, or 0 on error. Can be NULL. |

## Return Value

Returns A new frame of video on success, NULL if none is currently
available.

## Remarks

The frame is a memory pointer to the image data, whose size and format are
given by the spec requested when opening the device.

This is a non blocking API. If there is a frame available, a non-NULL
surface is returned, and timestampNS will be filled with a non-zero value.

Note that an error case can also return NULL, but a NULL by itself is
normal and just signifies that a new frame is not yet available. Note that
even if a camera device fails outright (a USB camera is unplugged while in
use, etc), SDL will send an event separately to notify the app, but
continue to provide blank frames at ongoing intervals until
[SDL_CloseCamera](SDL_CloseCamera)() is called, so real failure here is
almost always an out of memory condition.

After use, the frame should be released with
[SDL_ReleaseCameraFrame](SDL_ReleaseCameraFrame)(). If you don't do this,
the system may stop providing more video!

Do not call [SDL_FreeSurface](SDL_FreeSurface)() on the returned surface!
It must be given back to the camera subsystem with
[SDL_ReleaseCameraFrame](SDL_ReleaseCameraFrame)!

If the system is waiting for the user to approve access to the camera, as
some platforms require, this will return NULL (no frames available); you
should either wait for an
[SDL_EVENT_CAMERA_DEVICE_APPROVED](SDL_EVENT_CAMERA_DEVICE_APPROVED) (or
[SDL_EVENT_CAMERA_DEVICE_DENIED](SDL_EVENT_CAMERA_DEVICE_DENIED)) event, or
poll [SDL_IsCameraApproved](SDL_IsCameraApproved)() occasionally until it
returns non-zero.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_ReleaseCameraFrame](SDL_ReleaseCameraFrame)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

