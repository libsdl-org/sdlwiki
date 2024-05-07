###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Metal_GetDrawableSize

Get the size of a window's underlying drawable in pixels (for use with setting viewport, scissor & etc).

## Header File

Defined in [SDL_metal.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_metal.h)

## Syntax

```c
void SDL_Metal_GetDrawableSize(SDL_Window* window, int *w,
                               int *h);

```

## Function Parameters

|                |                                                                         |
| -------------- | ----------------------------------------------------------------------- |
| **window**     | [SDL_Window](SDL_Window) from which the drawable size should be queried |
| **w**          | Pointer to variable for storing the width in pixels, may be NULL        |
| **h**          | Pointer to variable for storing the height in pixels, may be NULL       |

## Version

This function is available since SDL 2.0.14.

## See Also

- [SDL_GetWindowSize](SDL_GetWindowSize)
- [SDL_CreateWindow](SDL_CreateWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

