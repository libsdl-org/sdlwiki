# SDL_SetRenderLogicalPresentation

Set a device-independent resolution and presentation mode for rendering.

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
The renderer will act as if the current render target is always the
requested dimensions, scaling to the actual resolution as necessary.

This can be useful for games that expect a fixed size, but would like to
scale the output to whatever is available, regardless of how a user resizes
a window, or if the display is high DPI.

Logical presentation can be used with both render target textures and the
renderer's window; the state is unique to each render target, and this
function sets the state for the current render target. It might be useful
to draw to a texture that matches the window dimensions with logical
presentation enabled, and then draw that texture across the entire window
with logical presentation disabled. Be careful not to render both with
logical presentation enabled, however, as this could produce
double-letterboxing, etc.

You can disable logical coordinates by setting the mode to
[SDL_LOGICAL_PRESENTATION_DISABLED](SDL_LOGICAL_PRESENTATION_DISABLED), and
in that case you get the full pixel resolution of the render target; it is
safe to toggle logical presentation during the rendering of a frame:
perhaps most of the rendering is done to specific dimensions but to make
fonts look sharp, the app turns off logical presentation while drawing
text, for example.

For the renderer's window, letterboxing is drawn into the framebuffer if
logical presentation is enabled during
[SDL_RenderPresent](SDL_RenderPresent); be sure to reenable it before
presenting if you were toggling it, otherwise the letterbox areas might
have artifacts from previous frames (or artifacts from external overlays,
etc). Letterboxing is never drawn into texture render targets; be sure to
call [SDL_RenderClear](SDL_RenderClear)() before drawing into the texture
so the letterboxing areas are cleared, if appropriate.

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

