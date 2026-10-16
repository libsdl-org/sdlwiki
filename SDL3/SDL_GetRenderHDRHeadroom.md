# SDL_GetRenderHDRHeadroom

Get the HDR headroom used for render output.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetRenderHDRHeadroom(SDL_Renderer *renderer, float *headroom);
```

## Function Parameters

|                                |              |                                                                     |
| ------------------------------ | ------------ | ------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                              |
| float *                        | **headroom** | a pointer filled in with the HDR headroom being used for rendering. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_SetRenderHDRHeadroom](SDL_SetRenderHDRHeadroom)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

