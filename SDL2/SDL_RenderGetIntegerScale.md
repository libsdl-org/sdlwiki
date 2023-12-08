###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetIntegerScale

Get whether integer scales are forced for resolution-independent rendering.

## Syntax

```c
SDL_bool SDL_RenderGetIntegerScale(SDL_Renderer * renderer);

```

## Function Parameters

|                  |                                                           |
| ---------------- | --------------------------------------------------------- |
| **renderer**     | the renderer from which integer scaling should be queried |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if integer scales are forced or
[SDL_FALSE](SDL_FALSE.md) if not and on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.5.

## Related Functions

* [SDL_RenderSetIntegerScale](SDL_RenderSetIntegerScale.md)

----
[CategoryAPI](CategoryAPI.md)
