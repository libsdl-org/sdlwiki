# SDL_SetSoftwareRendererWindow

Associate a software renderer with a window.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetSoftwareRendererWindow(SDL_Renderer *renderer, SDL_Window *window);
```

## Function Parameters

|                                |              |                                          |
| ------------------------------ | ------------ | ---------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                   |
| [SDL_Window](SDL_Window) *     | **window**   | the window where rendering is displayed. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_CreateSoftwareRenderer](SDL_CreateSoftwareRenderer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

