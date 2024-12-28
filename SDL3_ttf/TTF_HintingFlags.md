###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_HintingFlags

Hinting flags for TTF (TrueType Fonts)

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef enum TTF_HintingFlags
{
    TTF_HINTING_NORMAL = 0,     /**< Normal hinting applies standard grid-fitting. */
    TTF_HINTING_LIGHT,          /**< Light hinting applies subtle adjustments to improve rendering. */
    TTF_HINTING_MONO,           /**< Monochrome hinting adjusts the font for better rendering at lower resolutions. */
    TTF_HINTING_NONE,           /**< No hinting, the font is rendered without any grid-fitting. */
    TTF_HINTING_LIGHT_SUBPIXEL  /**< Light hinting with subpixel rendering for more precise font edges. */
} TTF_HintingFlags;
```

## Remarks

This enum specifies the level of hinting to be applied to the font
rendering. The hinting level determines how much the font's outlines are
adjusted for better alignment on the pixel grid.

## Version

This enum is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontHinting](TTF_SetFontHinting)
- [TTF_GetFontHinting](TTF_GetFontHinting)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySDLTTF](CategorySDLTTF)

