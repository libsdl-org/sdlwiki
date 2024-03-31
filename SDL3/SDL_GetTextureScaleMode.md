###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureScaleMode

Get the scale mode used for texture scale operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_GetTextureScaleMode(SDL_Texture *texture, SDL_ScaleMode *scaleMode);

```

## Function Parameters

|                   |                                                  |
| ----------------- | ------------------------------------------------ |
| **texture**       | the texture to query.                            |
| **scaleMode**     | a pointer filled in with the current scale mode. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetTextureScaleMode](SDL_SetTextureScaleMode)

----
[CategoryAPI](CategoryAPI)

