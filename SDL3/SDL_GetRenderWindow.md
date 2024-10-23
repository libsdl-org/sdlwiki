###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetRenderWindow

Get the window associated with a renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Window * SDL_GetRenderWindow(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer to query. |

## Return Value

([SDL_Window](SDL_Window) *) Returns the window on success or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

