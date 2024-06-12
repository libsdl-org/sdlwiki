###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderLogicalPresentation

Get device independent resolution and presentation mode for rendering.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_GetRenderLogicalPresentation(SDL_Renderer *renderer, float *w, float *h, SDL_RendererLogicalPresentation *mode, SDL_ScaleMode *scale_mode);
```

## Function Parameters

|                                                                      |                |                                                |
| -------------------------------------------------------------------- | -------------- | ---------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *                                       | **renderer**   | the rendering context                          |
| float *                                                              | **w**          | an int to be filled with the width             |
| float *                                                              | **h**          | an int to be filled with the height            |
| [SDL_RendererLogicalPresentation](SDL_RendererLogicalPresentation) * | **mode**       | a pointer filled in with the presentation mode |
| [SDL_ScaleMode](SDL_ScaleMode) *                                     | **scale_mode** | a pointer filled in with the scale mode        |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function gets the width and height of the logical rendering output, or
the output size in pixels if a logical resolution is not enabled.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

