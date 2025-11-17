###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontCharSpacing

Set additional space in pixels to be applied between any two rendered characters.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetFontCharSpacing(TTF_Font *font, int spacing);
```

## Function Parameters

|                        |             |                                                |
| ---------------------- | ----------- | ---------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**    | the font to specify a direction for.           |
| int                    | **spacing** | the new additional glyph spacing for the font. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

The spacing value is applied uniformly after each character, in addition to
the normal glyph's advance.

Spacing may be a negative value, in which case it will reduce the distance
instead.

This updates any [TTF_Text](TTF_Text) objects using this font.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

