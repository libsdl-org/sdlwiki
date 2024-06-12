###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRendererName

Get the name of a renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
const char* SDL_GetRendererName(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                       |
| ------------------------------ | ------------ | --------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context |

## Return Value

(const char *) Returns the name of the selected renderer, or NULL if the
renderer is invalid.

## Remarks

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateRenderer](SDL_CreateRenderer)
- [SDL_CreateRendererWithProperties](SDL_CreateRendererWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

