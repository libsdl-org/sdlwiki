###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVideoDriver

Get the name of a built in video driver.

## Syntax

```c
const char* SDL_GetVideoDriver(int index);

```

## Function Parameters

|               |                             |
| ------------- | --------------------------- |
| **index**     | the index of a video driver |

## Return Value

Returns the name of the video driver with the given **index**.

## Remarks

The video drivers are presented in the order in which they are normally
checked during initialization.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
