###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderLogicalPresentationRect

Get the final presentation rectangle for rendering.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_GetRenderLogicalPresentationRect(SDL_Renderer *renderer, SDL_FRect *rect);
```

## Function Parameters

|                                |              |                                                                         |
| ------------------------------ | ------------ | ----------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                  |
| [SDL_FRect](SDL_FRect) *       | **rect**     | a pointer filled in with the final presentation rectangle, may be NULL. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function returns the calculated rectangle used for logical
presentation, based on the presentation mode and output size. If logical
presentation is disabled, it will fill the rectangle with the output size,
in pixels.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

