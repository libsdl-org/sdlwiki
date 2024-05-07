###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRendererInfo

Get information about a rendering context.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_GetRendererInfo(SDL_Renderer * renderer,
                        SDL_RendererInfo * info);

```

## Function Parameters

|                  |                                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                |
| **info**         | an [SDL_RendererInfo](SDL_RendererInfo) structure filled with information about the current renderer |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateRenderer](SDL_CreateRenderer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

