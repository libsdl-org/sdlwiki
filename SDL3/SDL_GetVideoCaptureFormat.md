###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVideoCaptureFormat

Get frame format of video capture device.

## Syntax

```c
int SDL_GetVideoCaptureFormat(SDL_VideoCaptureDevice *device,
                              int index,
                              Uint32 *format);

```

## Function Parameters

|                |                                                                    |
| -------------- | ------------------------------------------------------------------ |
| **device**     | opened video capture device                                        |
| **index**      | format between 0 and num -1                                        |
| **format**     | pointer output format ([SDL_PixelFormatEnum](SDL_PixelFormatEnum)) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The value can be used to fill [SDL_VideoCaptureSpec](SDL_VideoCaptureSpec)
structure.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumVideoCaptureFormats](SDL_GetNumVideoCaptureFormats)

----
[CategoryAPI](CategoryAPI)

