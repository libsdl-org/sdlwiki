###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseCamera

Use this function to shut down camera processing and close the camera device.

## Header File

Defined in [SDL_camera.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
void SDL_CloseCamera(SDL_Camera *camera);

```

## Function Parameters

|                |                      |
| -------------- | -------------------- |
| **camera**     | opened camera device |

## Thread Safety

It is safe to call this function from any thread, but no thread may
reference `device` once this function is called.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_OpenCameraWithSpec](SDL_OpenCameraWithSpec)
* [SDL_OpenCamera](SDL_OpenCamera)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

