###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderReadPixels

Read pixels from the current rendering target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Surface * SDL_RenderReadPixels(SDL_Renderer *renderer, const SDL_Rect *rect);

```

## Function Parameters

|                  |                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                                                  |
| **rect**         | an [SDL_Rect](SDL_Rect) structure representing the area in pixels relative to the to current viewport, or NULL for the entire viewport |

## Return Value

Returns a new [SDL_Surface](SDL_Surface) on success or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The returned surface should be freed with
[SDL_DestroySurface](SDL_DestroySurface)()

**WARNING**: This is a very slow operation, and should not be used
frequently. If you're using this on the main rendering target, it should be
called after rendering and before [SDL_RenderPresent](SDL_RenderPresent)().

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)


