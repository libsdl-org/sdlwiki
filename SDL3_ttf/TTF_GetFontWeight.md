###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontWeight

Query a font's weight, in terms of the lightness/heaviness of the strokes.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
int TTF_GetFontWeight(const TTF_Font *font);


#define TTF_FONT_WEIGHT_THIN        100 /**< Thin (100) named font weight value */
#define TTF_FONT_WEIGHT_EXTRA_LIGHT 200 /**< ExtraLight (200) named font weight value */
#define TTF_FONT_WEIGHT_LIGHT       300 /**< Light (300) named font weight value */
#define TTF_FONT_WEIGHT_NORMAL      400 /**< Normal (400) named font weight value */
#define TTF_FONT_WEIGHT_MEDIUM      500 /**< Medium (500) named font weight value */
#define TTF_FONT_WEIGHT_SEMI_BOLD   600 /**< SemiBold (600) named font weight value */
#define TTF_FONT_WEIGHT_BOLD        700 /**< Bold (700) named font weight value */
#define TTF_FONT_WEIGHT_EXTRA_BOLD  800 /**< ExtraBold (800) named font weight value */
#define TTF_FONT_WEIGHT_BLACK       900 /**< Black (900) named font weight value */
#define TTF_FONT_WEIGHT_EXTRA_BLACK 950 /**< ExtraBlack (950) named font weight value */
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(int) Returns the font's current weight.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

