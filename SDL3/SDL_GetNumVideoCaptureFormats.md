###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumVideoCaptureFormats

Number of available formats for the device 

## Syntax

```c
int SDL_GetNumVideoCaptureFormats(SDL_VideoCaptureDevice *device);

```

## Function Parameters

|                |                             |
| -------------- | --------------------------- |
| **device**     | opened video capture device |

## Return Value

Returns number of formats or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetVideoCaptureFormat](SDL_GetVideoCaptureFormat)
* [SDL_SetVideoCaptureSpec](SDL_SetVideoCaptureSpec)

----
[CategoryAPI](CategoryAPI)

