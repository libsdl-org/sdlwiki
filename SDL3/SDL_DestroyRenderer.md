###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

You may only call this function from the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_CreateRenderer](SDL_CreateRenderer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

