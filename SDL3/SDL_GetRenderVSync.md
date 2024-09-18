###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderVSync

Get VSync of the given renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetRenderVSync(SDL_Renderer *renderer, int *vsync);
```

## Function Parameters

|                                |              |                                                                                                                                             |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer to toggle.                                                                                                                     |
| int *                          | **vsync**    | an int filled with the current vertical refresh sync interval. See [SDL_SetRenderVSync](SDL_SetRenderVSync)() for the meaning of the value. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetRenderVSync](SDL_SetRenderVSync)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

