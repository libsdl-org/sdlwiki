###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderTarget

Set a texture as the current rendering target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_SetRenderTarget(SDL_Renderer *renderer, SDL_Texture *texture);

```

## Function Parameters

|                  |                                                                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                                                                                   |
| **texture**      | the targeted texture, which must be created with the [`SDL_TEXTUREACCESS_TARGET`](SDL_TEXTUREACCESS_TARGET) flag, or NULL to render to the window instead of a texture. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The default render target is the window for which the renderer was created.
To stop rendering to a texture and render to the window again, call this
function with a NULL `texture`.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetRenderTarget](SDL_GetRenderTarget)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)


