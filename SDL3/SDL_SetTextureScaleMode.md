###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetTextureScaleMode

Set the scale mode used for texture scale operations.

## Syntax

```c
int SDL_SetTextureScaleMode(SDL_Texture *texture, SDL_ScaleMode scaleMode);

```

## Function Parameters

|                   |                                                                |
| ----------------- | -------------------------------------------------------------- |
| **texture**       | The texture to update.                                         |
| **scaleMode**     | the [SDL_ScaleMode](SDL_ScaleMode) to use for texture scaling. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The default texture scale mode is
[SDL_SCALEMODE_LINEAR](SDL_SCALEMODE_LINEAR).

If the scale mode is not supported, the closest supported mode is chosen.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetTextureScaleMode](SDL_GetTextureScaleMode)

----
[CategoryAPI](CategoryAPI)

