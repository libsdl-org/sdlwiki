# SDL_SetRenderLogicalPresentationRect

Set the final presentation rectangle for rendering.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderLogicalPresentationRect(SDL_Renderer *renderer, const SDL_FRect *rect);
```

## Function Parameters

|                                |              |                                                                                    |
| ------------------------------ | ------------ | ---------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                             |
| const [SDL_FRect](SDL_FRect) * | **rect**     | the presentation rectangle, in pixels, or NULL to stretch to the full output size. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function sets the rectangle used when the logical presentation mode is
[SDL_LOGICAL_PRESENTATION_CUSTOM](SDL_LOGICAL_PRESENTATION_CUSTOM).

The logical size is scaled to fit the rectangle, so if the rectangle has a
different aspect ratio than the logical size, the output will be stretched.
The rectangle is in pixels and may extend past the edges of the output.

Each render target has its own logical presentation state. This function
sets the rectangle for the current render target.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_GetRenderLogicalPresentationRect](SDL_GetRenderLogicalPresentationRect)
- [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

