###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CreateRendererTextEngine

Create a text engine for drawing text on an SDL renderer.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_TextEngine * TTF_CreateRendererTextEngine(SDL_Renderer *renderer);
```

## Function Parameters

|                |              |                                                             |
| -------------- | ------------ | ----------------------------------------------------------- |
| SDL_Renderer * | **renderer** | the renderer to use for creating textures and drawing text. |

## Return Value

([TTF_TextEngine](TTF_TextEngine) *) Returns a
[TTF_TextEngine](TTF_TextEngine) object or NULL on failure; call
SDL_GetError() for more information.

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_DestroyRendererTextEngine](TTF_DestroyRendererTextEngine)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

