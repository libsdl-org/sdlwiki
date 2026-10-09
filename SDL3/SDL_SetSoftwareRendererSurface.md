# SDL_SetSoftwareRendererSurface

Associate a software renderer with a surface.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetSoftwareRendererSurface(SDL_Renderer *renderer, SDL_Surface *surface);
```

## Function Parameters

|                                |              |                                      |
| ------------------------------ | ------------ | ------------------------------------ |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.               |
| [SDL_Surface](SDL_Surface) *   | **surface**  | the surface where rendering is done. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_CreateSoftwareRenderer](SDL_CreateSoftwareRenderer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

