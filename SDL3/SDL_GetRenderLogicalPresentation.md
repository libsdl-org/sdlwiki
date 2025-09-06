# SDL_GetRenderLogicalPresentation

Get device independent resolution and presentation mode for rendering.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetRenderLogicalPresentation(SDL_Renderer *renderer, int *w, int *h, SDL_RendererLogicalPresentation *mode);
```

## Function Parameters

|                                                                      |              |                                                                  |
| -------------------------------------------------------------------- | ------------ | ---------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *                                       | **renderer** | the rendering context.                                           |
| int *                                                                | **w**        | an int filled with the logical presentation width.               |
| int *                                                                | **h**        | an int filled with the logical presentation height.              |
| [SDL_RendererLogicalPresentation](SDL_RendererLogicalPresentation) * | **mode**     | a variable filled with the logical presentation mode being used. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function gets the width and height of the logical rendering output, or
0 if a logical resolution is not enabled.

Each render target has its own logical presentation state. This function
gets the state for the current render target.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

