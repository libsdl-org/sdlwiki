###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureScaleMode

Get the scale mode used for texture scale operations.

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

