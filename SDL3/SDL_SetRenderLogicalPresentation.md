# SDL_SetRenderLogicalPresentation

Set a device independent resolution and presentation mode for rendering.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderLogicalPresentation(SDL_Renderer *renderer, int w, int h, SDL_RendererLogicalPresentation mode);
```

## Function Parameters

|                                                                    |              |                                       |
| ------------------------------------------------------------------ | ------------ | ------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *                                     | **renderer** | the rendering context.                |
| int                                                                | **w**        | the width of the logical resolution.  |
| int                                                                | **h**        | the height of the logical resolution. |
| [SDL_RendererLogicalPresentation](SDL_RendererLogicalPresentation) | **mode**     | the presentation mode used.           |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function sets the width and height of the logical rendering output.
The renderer will act as if the window is always the requested dimensions,
scaling to the actual window resolution as necessary.

This can be useful for games that expect a fixed size, but would like to
scale the output to whatever is available, regardless of how a user resizes
a window, or if the display is high DPI.

You can disable logical coordinates by setting the mode to
[SDL_LOGICAL_PRESENTATION_DISABLED](SDL_LOGICAL_PRESENTATION_DISABLED), and
in that case you get the full pixel resolution of the output window; it is
safe to toggle logical presentation during the rendering of a frame:
perhaps most of the rendering is done to specific dimensions but to make
fonts look sharp, the app turns off logical presentation while drawing
text.

Letterboxing will only happen if logical presentation is enabled during
[SDL_RenderPresent](SDL_RenderPresent); be sure to reenable it first if you
were using it.

You can convert coordinates in an event into rendering coordinates using
[SDL_ConvertEventToRenderCoordinates](SDL_ConvertEventToRenderCoordinates)().

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_ConvertEventToRenderCoordinates](SDL_ConvertEventToRenderCoordinates)
- [SDL_GetRenderLogicalPresentation](SDL_GetRenderLogicalPresentation)
- [SDL_GetRenderLogicalPresentationRect](SDL_GetRenderLogicalPresentationRect)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

