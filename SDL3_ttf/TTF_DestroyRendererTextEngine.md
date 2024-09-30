###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_DestroyRendererTextEngine

Destroy a text engine created for drawing text on an SDL renderer.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_DestroyRendererTextEngine(TTF_TextEngine *engine);
```

## Function Parameters

|                                    |            |                                                                                                                        |
| ---------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| [TTF_TextEngine](TTF_TextEngine) * | **engine** | a [TTF_TextEngine](TTF_TextEngine) object created with [TTF_CreateRendererTextEngine](TTF_CreateRendererTextEngine)(). |

## Remarks

All text created by this engine should be destroyed before calling this
function.

## Thread Safety

This function should be called on the thread that created the engine.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CreateRendererTextEngine](TTF_CreateRendererTextEngine)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

