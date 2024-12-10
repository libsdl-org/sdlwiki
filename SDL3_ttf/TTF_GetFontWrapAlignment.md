###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontWrapAlignment

Query a font's current wrap alignment option.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_HorizontalAlignment TTF_GetFontWrapAlignment(const TTF_Font *font);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

([TTF_HorizontalAlignment](TTF_HorizontalAlignment)) Returns the font's
current wrap alignment option.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontWrapAlignment](TTF_SetFontWrapAlignment)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

