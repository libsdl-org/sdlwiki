###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderVSync

Toggle VSync of the given renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_SetRenderVSync(SDL_Renderer *renderer, int vsync);

```

## Function Parameters

|                  |                                                                                                                                                                                                                                                                                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | The renderer to toggle                                                                                                                                                                                                                                                                                                                             |
| **vsync**        | the vertical refresh sync interval, 1 to synchronize present with every vertical refresh, 2 to synchronize present with every second vertical refresh, etc., or -1 for late swap tearing (adaptive vsync). Not every value is supported by every renderer, so you should check the return value to see whether the requested setting is supported. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetRenderVSync](SDL_GetRenderVSync)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

