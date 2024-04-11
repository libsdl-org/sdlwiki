###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsShapedWindow

Return whether the given window is a shaped window.

## Header File

Defined in [SDL_shape.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_shape.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_IsShapedWindow(const SDL_Window *window);

```

## Function Parameters

|                |                                       |
| -------------- | ------------------------------------- |
| **window**     | The window to query for being shaped. |

## Return Value

Return [SDL_TRUE](SDL_TRUE) if the window is a window that can be shaped,
[SDL_FALSE](SDL_FALSE) if the window is unshaped or NULL.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_CreateShapedWindow](SDL_CreateShapedWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

