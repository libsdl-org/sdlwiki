# SDL_DestroyRenderer

Destroy the rendering context for a window and free all associated textures.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
void SDL_DestroyRenderer(SDL_Renderer *renderer);
```

## Function Parameters

|                            |              |                          |
| -------------------------- | ------------ | ------------------------ |
| [SDL_Render](SDL_Render) * | **renderer** | the renderer to destroy. |


## Remarks

This should be called before destroying the associated window.

## Version

This function is available since SDL 3.0.0.


## See Also

- [SDL_CreateRenderer](https://wiki.libsdl.org/SDL3/SDL_CreateRenderer)