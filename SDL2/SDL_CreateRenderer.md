###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateRenderer

Create a 2D rendering context for a window.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
SDL_Renderer * SDL_CreateRenderer(SDL_Window * window,
                   int index, Uint32 flags);
```

## Function Parameters

|                            |            |                                                                                                                    |
| -------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------ |
| [SDL_Window](SDL_Window) * | **window** | the window where rendering is displayed.                                                                           |
| int                        | **index**  | the index of the rendering driver to initialize, or -1 to initialize the first one supporting the requested flags. |
| Uint32                     | **flags**  | 0, or one or more [SDL_RendererFlags](SDL_RendererFlags) OR'd together.                                            |

## Return Value

([SDL_Renderer](SDL_Renderer) *) Returns a valid rendering context or NULL
if there was an error; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateSoftwareRenderer](SDL_CreateSoftwareRenderer)
- [SDL_DestroyRenderer](SDL_DestroyRenderer)
- [SDL_GetNumRenderDrivers](SDL_GetNumRenderDrivers)
- [SDL_GetRendererInfo](SDL_GetRendererInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

