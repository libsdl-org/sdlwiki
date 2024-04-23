###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowData

Retrieve the data pointer associated with a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void* SDL_GetWindowData(SDL_Window * window,
                        const char *name);

```

## Function Parameters

|                |                         |
| -------------- | ----------------------- |
| **window**     | the window to query     |
| **name**       | the name of the pointer |

## Return Value

Returns the value associated with `name`.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetWindowData](SDL_SetWindowData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


