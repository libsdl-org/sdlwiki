###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumVideoCaptureFrameSizes

Number of different framesizes available for the device and pixel format.

## Syntax

```c
int SDL_GetNumVideoCaptureFrameSizes(SDL_VideoCaptureDevice *device, Uint32 format);

```

## Function Parameters

|                |                                                                 |
| -------------- | --------------------------------------------------------------- |
| **device**     | opened video capture device                                     |
| **format**     | frame pixel format ([SDL_PixelFormatEnum](SDL_PixelFormatEnum)) |

## Return Value

Returns number of framesizes or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetVideoCaptureFrameSize](SDL_GetVideoCaptureFrameSize)
* [SDL_SetVideoCaptureSpec](SDL_SetVideoCaptureSpec)

----
[CategoryAPI](CategoryAPI)

