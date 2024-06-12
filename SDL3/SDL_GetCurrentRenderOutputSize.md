###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentRenderOutputSize

Get the current output size in pixels of a rendering context.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_GetCurrentRenderOutputSize(SDL_Renderer *renderer, float *w, float *h);
```

## Function Parameters

|                  |                                             |
| ---------------- | ------------------------------------------- |
| **renderer**     | the rendering context                       |
| **w**            | a pointer filled in with the current width  |
| **h**            | a pointer filled in with the current height |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If a rendering target is active, this will return the size of the rendering
target in pixels, otherwise if a logical size is set, it will return the
logical size, otherwise it will return the value of
[SDL_GetRenderOutputSize](SDL_GetRenderOutputSize)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetRenderOutputSize](SDL_GetRenderOutputSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

