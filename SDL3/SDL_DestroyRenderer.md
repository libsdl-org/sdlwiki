###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyRenderer

Destroy the rendering context for a window and free all associated textures.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
void SDL_DestroyRenderer(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context. |

## Remarks

This should be called before destroying the associated window.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateRenderer](SDL_CreateRenderer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

