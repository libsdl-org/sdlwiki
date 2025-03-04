# SDL_RenderPresent

Update the screen with any rendering performed since the previous call.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderPresent(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL's rendering functions operate on a backbuffer; that is, calling a
rendering function such as [SDL_RenderLine](SDL_RenderLine)() does not
directly put a line on the screen, but rather updates the backbuffer. As
such, you compose your entire scene and *present* the composed backbuffer
to the screen as a complete picture.

Therefore, when using SDL's rendering API, one does all drawing intended
for the frame, and then calls this function once per frame to present the
final drawing to the user.

The backbuffer should be considered invalidated after each present; do not
assume that previous contents will exist between frames. You are strongly
encouraged to call [SDL_RenderClear](SDL_RenderClear)() to initialize the
backbuffer before starting each new frame's drawing, even if you plan to
overwrite every pixel.

Please note, that in case of rendering to a texture - there is **no need**
to call [`SDL_RenderPresent`](SDL_RenderPresent) after drawing needed
objects to a texture, and should not be done; you are only required to
change back the rendering target to default via
`SDL_SetRenderTarget(renderer, NULL)` afterwards, as textures by themselves
do not have a concept of backbuffers. Calling
[SDL_RenderPresent](SDL_RenderPresent) while rendering to a texture will
fail.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateRenderer](SDL_CreateRenderer)
- [SDL_RenderClear](SDL_RenderClear)
- [SDL_RenderFillRect](SDL_RenderFillRect)
- [SDL_RenderFillRects](SDL_RenderFillRects)
- [SDL_RenderLine](SDL_RenderLine)
- [SDL_RenderLines](SDL_RenderLines)
- [SDL_RenderPoint](SDL_RenderPoint)
- [SDL_RenderPoints](SDL_RenderPoints)
- [SDL_RenderRect](SDL_RenderRect)
- [SDL_RenderRects](SDL_RenderRects)
- [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)
- [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

