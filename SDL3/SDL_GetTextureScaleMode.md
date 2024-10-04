###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTextureScaleMode

Get the scale mode used for texture scale operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetTextureScaleMode(SDL_Texture *texture, SDL_ScaleMode *scaleMode);
```

## Function Parameters

|                                  |               |                                                  |
| -------------------------------- | ------------- | ------------------------------------------------ |
| [SDL_Texture](SDL_Texture) *     | **texture**   | the texture to query.                            |
| [SDL_ScaleMode](SDL_ScaleMode) * | **scaleMode** | a pointer filled in with the current scale mode. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetTextureScaleMode](SDL_SetTextureScaleMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

