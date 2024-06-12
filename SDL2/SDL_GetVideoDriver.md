###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetVideoDriver

Get the name of a built in video driver.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
const char* SDL_GetVideoDriver(int index);
```

## Function Parameters

|     |           |                             |
| --- | --------- | --------------------------- |
| int | **index** | the index of a video driver |

## Return Value

(const char *) Returns the name of the video driver with the given
**index**.

## Remarks

The video drivers are presented in the order in which they are normally
checked during initialization.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

