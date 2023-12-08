###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderPresent

Update the screen with any rendering performed since the previous call.

## Syntax

```c
int SDL_RenderPresent(SDL_Renderer *renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

SDL's rendering functions operate on a backbuffer; that is, calling a
rendering function such as [SDL_RenderLine](SDL_RenderLine.md)() does not
directly put a line on the screen, but rather updates the backbuffer. As
such, you compose your entire scene and *present* the composed backbuffer
to the screen as a complete picture.

Therefore, when using SDL's rendering API, one does all drawing intended
for the frame, and then calls this function once per frame to present the
final drawing to the user.

The backbuffer should be considered invalidated after each present; do not
assume that previous contents will exist between frames. You are strongly
encouraged to call [SDL_RenderClear](SDL_RenderClear.md)() to initialize the
backbuffer before starting each new frame's drawing, even if you plan to
overwrite every pixel.

## Thread Safety

You may only call this function on the main thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

Please refer to the code example in [SDL_RenderClear](SDL_RenderClear.md).

## Related Functions

* [SDL_RenderClear](SDL_RenderClear.md)
* [SDL_RenderLine](SDL_RenderLine.md)
* [SDL_RenderLines](SDL_RenderLines.md)
* [SDL_RenderPoint](SDL_RenderPoint.md)
* [SDL_RenderPoints](SDL_RenderPoints.md)
* [SDL_RenderRect](SDL_RenderRect.md)
* [SDL_RenderRects](SDL_RenderRects.md)
* [SDL_RenderFillRect](SDL_RenderFillRect.md)
* [SDL_RenderFillRects](SDL_RenderFillRects.md)
* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode.md)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
