###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRendererFromTexture

Get the renderer that created an [SDL_Texture](SDL_Texture).

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_Renderer* SDL_GetRendererFromTexture(SDL_Texture *texture);

```

## Function Parameters

|                 |                      |
| --------------- | -------------------- |
| **texture**     | the texture to query |

## Return Value

Returns a pointer to the [SDL_Renderer](SDL_Renderer) that created the
texture, or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

