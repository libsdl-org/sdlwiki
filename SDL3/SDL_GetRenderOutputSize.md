###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderOutputSize

Get the output size in pixels of a rendering context.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_GetRenderOutputSize(SDL_Renderer *renderer, int *w, int *h);
```

## Function Parameters

|                                |              |                                                |
| ------------------------------ | ------------ | ---------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                         |
| int *                          | **w**        | a pointer filled in with the width in pixels.  |
| int *                          | **h**        | a pointer filled in with the height in pixels. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This returns the true output size in pixels, ignoring any render targets or
logical size and presentation.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetCurrentRenderOutputSize](SDL_GetCurrentRenderOutputSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

