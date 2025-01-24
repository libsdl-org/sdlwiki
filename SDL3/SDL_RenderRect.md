# SDL_RenderRect

Draw a rectangle on the current rendering target at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderRect(SDL_Renderer *renderer, const SDL_FRect *rect);
```

## Function Parameters

|                                |              |                                                                                         |
| ------------------------------ | ------------ | --------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer which should draw a rectangle.                                             |
| const [SDL_FRect](SDL_FRect) * | **rect**     | a pointer to the destination rectangle, or NULL to outline the entire rendering target. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RenderRects](SDL_RenderRects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

