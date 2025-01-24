# SDL_GetCurrentRenderOutputSize

Get the current output size in pixels of a rendering context.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetCurrentRenderOutputSize(SDL_Renderer *renderer, int *w, int *h);
```

## Function Parameters

|                                |              |                                              |
| ------------------------------ | ------------ | -------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                       |
| int *                          | **w**        | a pointer filled in with the current width.  |
| int *                          | **h**        | a pointer filled in with the current height. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If a rendering target is active, this will return the size of the rendering
target in pixels, otherwise if a logical size is set, it will return the
logical size, otherwise it will return the value of
[SDL_GetRenderOutputSize](SDL_GetRenderOutputSize)().

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetRenderOutputSize](SDL_GetRenderOutputSize)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

