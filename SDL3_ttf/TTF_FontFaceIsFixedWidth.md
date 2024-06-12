###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_FontFaceIsFixedWidth

Query whether a font is fixed-width.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
int TTF_FontFaceIsFixedWidth(const TTF_Font *font);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(int) Returns non-zero if fixed-width, zero if not.

## Remarks

A "fixed-width" font means all glyphs are the same width across; a
lowercase 'i' will be the same size across as a capital 'W', for example.
This is common for terminals and text editors, and other apps that treat
text as a grid. Most other things (WYSIWYG word processors, web pages, etc)
are more likely to not be fixed-width in most cases.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

