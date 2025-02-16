###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontSDF

Enable Signed Distance Field rendering for a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetFontSDF(TTF_Font *font, bool enabled);
```

## Function Parameters

|                        |             |                                       |
| ---------------------- | ----------- | ------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**    | the font to set SDF support on.       |
| bool                   | **enabled** | true to enable SDF, false to disable. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

SDF is a technique that helps fonts look sharp even when scaling and
rotating, and requires special shader support for display.

This works with Blended APIs, and generates the raw signed distance values
in the alpha channel of the resulting texture.

This updates any [TTF_Text](TTF_Text) objects using this font, and clears
already-generated glyphs, if any, from the cache.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetFontSDF](TTF_GetFontSDF)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

