###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetIntegerScale

Get whether integer scales are forced for resolution-independent rendering.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
SDL_bool SDL_RenderGetIntegerScale(SDL_Renderer * renderer);
```

## Function Parameters

|                                |              |                                                            |
| ------------------------------ | ------------ | ---------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer from which integer scaling should be queried. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if integer scales are
forced or [SDL_FALSE](SDL_FALSE) if not and on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.5.

## See Also

- [SDL_RenderSetIntegerScale](SDL_RenderSetIntegerScale)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

