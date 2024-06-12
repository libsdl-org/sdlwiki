###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateWindowAndRenderer

Create a window and default renderer.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_CreateWindowAndRenderer(
    int width, int height, Uint32 window_flags,
    SDL_Window **window, SDL_Renderer **renderer);
```

## Function Parameters

|                                 |                  |                                                                                  |
| ------------------------------- | ---------------- | -------------------------------------------------------------------------------- |
| int                             | **width**        | the width of the window                                                          |
| int                             | **height**       | the height of the window                                                         |
| Uint32                          | **window_flags** | the flags used to create the window (see [SDL_CreateWindow](SDL_CreateWindow)()) |
| [SDL_Window](SDL_Window) **     | **window**       | a pointer filled with the window, or NULL on error                               |
| [SDL_Renderer](SDL_Renderer) ** | **renderer**     | a pointer filled with the renderer, or NULL on error                             |

## Return Value

(int) Returns 0 on success, or -1 on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateRenderer](SDL_CreateRenderer)
- [SDL_CreateWindow](SDL_CreateWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

