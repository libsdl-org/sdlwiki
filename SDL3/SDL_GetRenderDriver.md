###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderDriver

Use this function to get the name of a built in 2D rendering driver.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
const char* SDL_GetRenderDriver(int index);

```

## Function Parameters

|               |                                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **index**     | the index of the rendering driver; the value ranges from 0 to [SDL_GetNumRenderDrivers](SDL_GetNumRenderDrivers)() - 1 |

## Return Value

Returns the name of the rendering driver at the requested index, or NULL if
an invalid index was specified.

## Remarks

The list of rendering drivers is given in the order that they are normally
initialized by default; the drivers that seem more reasonable to choose
first (as far as the SDL developers believe) are earlier in the list.

The names of drivers are all simple, low-ASCII identifiers, like "opengl",
"direct3d12" or "metal". These never have Unicode characters, and are not
meant to be proper names.

The returned value points to a static, read-only string; do not modify or
free it!

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetNumRenderDrivers](SDL_GetNumRenderDrivers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

