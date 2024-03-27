###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyRenderer

Destroy the rendering context for a window and free associated textures.

## Syntax

```c
void SDL_DestroyRenderer(SDL_Renderer *renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Remarks

If `renderer` is NULL, this function will return immediately after setting
the SDL error message to "Invalid renderer". See
[SDL_GetError](SDL_GetError)().

Note that destroying a window implicitly destroys the associated renderer,
so this should not be called if the window associated with the renderer has
already been destroyed.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer)

----
[CategoryAPI](CategoryAPI), [CategoryRender](CategoryRender)


