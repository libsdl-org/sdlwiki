###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontProperties

Get the properties associated with a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_PropertiesID TTF_GetFontProperties(TTF_Font *font);


#define TTF_PROP_FONT_OUTLINE_LINE_CAP_NUMBER           "SDL_ttf.font.outline.line_cap"
#define TTF_PROP_FONT_OUTLINE_LINE_JOIN_NUMBER          "SDL_ttf.font.outline.line_join"
#define TTF_PROP_FONT_OUTLINE_MITER_LIMIT_NUMBER        "SDL_ttf.font.outline.miter_limit"
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(SDL_PropertiesID) Returns a valid property ID on success or 0 on failure;
call SDL_GetError() for more information.

## Remarks

The following read-write properties are provided by SDL:

- [`TTF_PROP_FONT_OUTLINE_LINE_CAP_NUMBER`](TTF_PROP_FONT_OUTLINE_LINE_CAP_NUMBER):
  The FT_Stroker_LineCap value used when setting the font outline, defaults
  to `FT_STROKER_LINECAP_ROUND`.
- [`TTF_PROP_FONT_OUTLINE_LINE_JOIN_NUMBER`](TTF_PROP_FONT_OUTLINE_LINE_JOIN_NUMBER):
  The FT_Stroker_LineJoin value used when setting the font outline,
  defaults to `FT_STROKER_LINEJOIN_ROUND`.
- [`TTF_PROP_FONT_OUTLINE_MITER_LIMIT_NUMBER`](TTF_PROP_FONT_OUTLINE_MITER_LIMIT_NUMBER):
  The FT_Fixed miter limit used when setting the font outline, defaults to
  0.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

