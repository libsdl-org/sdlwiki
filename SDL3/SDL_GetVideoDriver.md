###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetVideoDriver

Get the name of a built in video driver.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const char * SDL_GetVideoDriver(int index);
```

## Function Parameters

|     |           |                              |
| --- | --------- | ---------------------------- |
| int | **index** | the index of a video driver. |

## Return Value

(const char *) Returns the name of the video driver with the given
**index**.

## Remarks

The video drivers are presented in the order in which they are normally
checked during initialization.

The names of drivers are all simple, low-ASCII identifiers, like "cocoa",
"x11" or "windows". These never have Unicode characters, and are not meant
to be proper names.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

