###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetRenderDrawBlendMode

Get the blend mode used for drawing operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetRenderDrawBlendMode(SDL_Renderer *renderer, SDL_BlendMode *blendMode);
```

## Function Parameters

|                                  |               |                                                                      |
| -------------------------------- | ------------- | -------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *   | **renderer**  | the rendering context.                                               |
| [SDL_BlendMode](SDL_BlendMode) * | **blendMode** | a pointer filled in with the current [SDL_BlendMode](SDL_BlendMode). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

