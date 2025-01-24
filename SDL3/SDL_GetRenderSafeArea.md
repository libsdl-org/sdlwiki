# SDL_GetRenderSafeArea

Get the safe area for rendering within the current viewport.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetRenderSafeArea(SDL_Renderer *renderer, SDL_Rect *rect);
```

## Function Parameters

|                                |              |                                                                         |
| ------------------------------ | ------------ | ----------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                  |
| [SDL_Rect](SDL_Rect) *         | **rect**     | a pointer filled in with the area that is safe for interactive content. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Some devices have portions of the screen which are partially obscured or
not interactive, possibly due to on-screen controls, curved edges, camera
notches, TV overscan, etc. This function provides the area of the current
viewport which is safe to have interactible content. You should continue
rendering into the rest of the render target, but it should not contain
visually important or interactible content.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

