###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVideoCaptureSpec

Get the obtained video capture spec 

## Syntax

```c
int SDL_GetVideoCaptureSpec(SDL_VideoCaptureDevice *device, SDL_VideoCaptureSpec *spec);

```

## Function Parameters

|                |                                                                                      |
| -------------- | ------------------------------------------------------------------------------------ |
| **device**     | opened video capture device                                                          |
| **spec**       | The [SDL_VideoCaptureSpec](SDL_VideoCaptureSpec) to be initialized by this function. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetVideoCaptureSpec](SDL_SetVideoCaptureSpec)
* [SDL_OpenVideoCaptureWithSpec](SDL_OpenVideoCaptureWithSpec)

----
[CategoryAPI](CategoryAPI)

