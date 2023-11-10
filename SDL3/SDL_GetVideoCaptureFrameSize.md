###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVideoCaptureFrameSize

Get frame sizes of the device and the specified input format.

## Syntax

```c
int SDL_GetVideoCaptureFrameSize(SDL_VideoCaptureDevice *device, Uint32 format, int index, int *width, int *height);

```

## Function Parameters

|                |                                                                                      |
| -------------- | ------------------------------------------------------------------------------------ |
| **device**     | opened video capture device                                                          |
| **format**     | a format that can be used by the device ([SDL_PixelFormatEnum](SDL_PixelFormatEnum)) |
| **index**      | framesize between 0 and num -1                                                       |
| **width**      | output width                                                                         |
| **height**     | output height                                                                        |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The value can be used to fill [SDL_VideoCaptureSpec](SDL_VideoCaptureSpec)
structure.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumVideoCaptureFrameSizes](SDL_GetNumVideoCaptureFrameSizes)

----
[CategoryAPI](CategoryAPI)

