###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderVSync

Get VSync of the given renderer.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_GetRenderVSync(SDL_Renderer *renderer, int *vsync);

```

## Function Parameters

|                  |                                                                       |
| ---------------- | --------------------------------------------------------------------- |
| **renderer**     | The renderer to toggle                                                |
| **vsync**        | an int filled with 1 for on, 0 for off. All other values are reserved |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetRenderVSync](SDL_SetRenderVSync)

----
[CategoryAPI](CategoryAPI)

