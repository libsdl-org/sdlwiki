###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseVideoCapture

Use this function to shut down video_capture processing and close the video_capture device.

## Syntax

```c
void SDL_CloseVideoCapture(SDL_VideoCaptureDevice *device);

```

## Function Parameters

|                |                             |
| -------------- | --------------------------- |
| **device**     | opened video capture device |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenVideoCaptureWithSpec](SDL_OpenVideoCaptureWithSpec)
* [SDL_OpenVideoCapture](SDL_OpenVideoCapture)

----
[CategoryAPI](CategoryAPI)

