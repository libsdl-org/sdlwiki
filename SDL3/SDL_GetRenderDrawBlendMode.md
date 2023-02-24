###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderDrawBlendMode

Get the blend mode used for drawing operations.

## Syntax

```c
int SDL_GetRenderDrawBlendMode(SDL_Renderer *renderer, SDL_BlendMode *blendMode);

```

## Function Parameters

|                   |                                                                     |
| ----------------- | ------------------------------------------------------------------- |
| **renderer**      | the rendering context                                               |
| **blendMode**     | a pointer filled in with the current [SDL_BlendMode](SDL_BlendMode) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryRender](CategoryRender)


