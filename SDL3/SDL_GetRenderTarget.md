###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetRenderTarget

Get the current render target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Texture * SDL_GetRenderTarget(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context. |

## Return Value

([SDL_Texture](SDL_Texture) *) Returns the current render target or NULL
for the default render target.

## Remarks

The default render target is the window for which the renderer was created,
and is reported a NULL here.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetRenderTarget](SDL_SetRenderTarget)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

