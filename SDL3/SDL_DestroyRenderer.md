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

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateRenderer](SDL_CreateRenderer)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

