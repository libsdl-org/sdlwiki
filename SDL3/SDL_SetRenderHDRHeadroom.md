# SDL_SetRenderHDRHeadroom

Set the HDR headroom for render output.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderHDRHeadroom(SDL_Renderer *renderer, float headroom);
```

## Function Parameters

|                                |              |                                                           |
| ------------------------------ | ------------ | --------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                    |
| float                          | **headroom** | the HDR headroom to use, or 0 to use the window headroom. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The HDR headroom is used to set the HDR metadata for HDR10 output and for
tone mapping textures that are set to a higher headroom.

By default the HDR headroom comes from the window associated with the
renderer, but this function allows you to override that and set a specific
value.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_GetRenderHDRHeadroom](SDL_GetRenderHDRHeadroom)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

