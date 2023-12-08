###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderPresent

Update the screen with any rendering performed since the previous call.

## Syntax

```c
void SDL_RenderPresent(SDL_Renderer * renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Remarks

SDL's rendering functions operate on a backbuffer; that is, calling a
rendering function such as [SDL_RenderDrawLine](SDL_RenderDrawLine.md)() does
not directly put a line on the screen, but rather updates the backbuffer.
As such, you compose your entire scene and *present* the composed
backbuffer to the screen as a complete picture.

Therefore, when using SDL's rendering API, one does all drawing intended
for the frame, and then calls this function once per frame to present the
final drawing to the user.

The backbuffer should be considered invalidated after each present; do not
assume that previous contents will exist between frames. You are strongly
encouraged to call [SDL_RenderClear](SDL_RenderClear.md)() to initialize the
backbuffer before starting each new frame's drawing, even if you plan to
overwrite every pixel.

## Thread Safety

You may only call this function on the main thread. If this happens to work
on a background thread on any given platform or backend, it's purely by
luck and you should not rely on it to work next time.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderClear](SDL_RenderClear.md)
* [SDL_RenderDrawLine](SDL_RenderDrawLine.md)
* [SDL_RenderDrawLines](SDL_RenderDrawLines.md)
* [SDL_RenderDrawPoint](SDL_RenderDrawPoint.md)
* [SDL_RenderDrawPoints](SDL_RenderDrawPoints.md)
* [SDL_RenderDrawRect](SDL_RenderDrawRect.md)
* [SDL_RenderDrawRects](SDL_RenderDrawRects.md)
* [SDL_RenderFillRect](SDL_RenderFillRect.md)
* [SDL_RenderFillRects](SDL_RenderFillRects.md)
* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode.md)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor.md)

----
[CategoryAPI](CategoryAPI.md)
