###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontLineSkip

Query the spacing between lines of text for a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
int TTF_GetFontLineSkip(const TTF_Font *font);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(int) Returns the font's recommended spacing.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontLineSkip](TTF_SetFontLineSkip)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

