###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetRenderLogicalPresentationRect

Get the final presentation rectangle for rendering.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetRenderLogicalPresentationRect(SDL_Renderer *renderer, SDL_FRect *rect);
```

## Function Parameters

|                                |              |                                                                         |
| ------------------------------ | ------------ | ----------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                  |
| [SDL_FRect](SDL_FRect) *       | **rect**     | a pointer filled in with the final presentation rectangle, may be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function returns the calculated rectangle used for logical
presentation, based on the presentation mode and output size. If logical
presentation is disabled, it will fill the rectangle with the output size,
in pixels.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

