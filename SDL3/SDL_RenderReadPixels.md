# SDL_RenderReadPixels

Read pixels from the current rendering target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Surface * SDL_RenderReadPixels(SDL_Renderer *renderer, const SDL_Rect *rect);
```

## Function Parameters

|                                |              |                                                                                                                                                  |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                                           |
| const [SDL_Rect](SDL_Rect) *   | **rect**     | an [SDL_Rect](SDL_Rect) structure representing the area to read, which will be clipped to the current viewport, or NULL for the entire viewport. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns a new [SDL_Surface](SDL_Surface) on
success or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The returned surface contains pixels inside the desired area clipped to the
current viewport, and should be freed with
[SDL_DestroySurface](SDL_DestroySurface)().

Note that this returns the actual pixels on the screen, so if you are using
logical presentation you should use
[SDL_GetRenderLogicalPresentationRect](SDL_GetRenderLogicalPresentationRect)()
to get the area containing your content.

**WARNING**: This is a very slow operation, and should not be used
frequently. If you're using this on the main rendering target, it should be
called after rendering and before [SDL_RenderPresent](SDL_RenderPresent)().

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

