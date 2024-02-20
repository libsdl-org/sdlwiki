###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseCamera

Use this function to shut down camera processing and close the camera device.

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

## Related Functions

* [SDL_OpenCameraWithSpec](SDL_OpenCameraWithSpec)
* [SDL_OpenCamera](SDL_OpenCamera)

----
[CategoryAPI](CategoryAPI)

