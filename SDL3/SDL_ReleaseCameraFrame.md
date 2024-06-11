###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReleaseCameraFrame

Release a frame of video acquired from a camera.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
int SDL_ReleaseCameraFrame(SDL_Camera *camera, SDL_Surface *frame);
```

## Function Parameters

|                |                                     |
| -------------- | ----------------------------------- |
| **camera**     | opened camera device                |
| **frame**      | The video frame surface to release. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Let the back-end re-use the internal buffer for camera.

This function _must_ be called only on surface objects returned by
[SDL_AcquireCameraFrame](SDL_AcquireCameraFrame)(). This function should be
called as quickly as possible after acquisition, as SDL keeps a small FIFO
queue of surfaces for video frames; if surfaces aren't released in a timely
manner, SDL may drop upcoming video frames from the camera.

If the app needs to keep the surface for a significant time, they should
make a copy of it and release the original.

The app should not use the surface again after calling this function;
assume the surface is freed and the pointer is invalid.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AcquireCameraFrame](SDL_AcquireCameraFrame)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

