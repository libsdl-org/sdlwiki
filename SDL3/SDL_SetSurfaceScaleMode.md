###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetSurfaceScaleMode

Set the scale mode used for surface scale operations.

## Syntax

```c
int SDL_SetSurfaceScaleMode(SDL_Surface *surface, SDL_ScaleMode scaleMode);

```

## Function Parameters

|                   |                                                        |
| ----------------- | ------------------------------------------------------ |
| **surface**       | the surface to update.                                 |
| **scaleMode**     | the [SDL_ScaleMode](SDL_ScaleMode) to use for scaling. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetSurfaceScaleMode](SDL_GetSurfaceScaleMode)
* [SDL_BlitSurfaceScaled](SDL_BlitSurfaceScaled)

----
[CategoryAPI](CategoryAPI)

