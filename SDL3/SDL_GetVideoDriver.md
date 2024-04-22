###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVideoDriver

Get the name of a built in video driver.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

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

## See Also

* [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)


