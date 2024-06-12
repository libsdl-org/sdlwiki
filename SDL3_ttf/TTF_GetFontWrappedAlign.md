###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontWrappedAlign

Query a font's current wrap alignment option.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
int TTF_GetFontWrappedAlign(const TTF_Font *font);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(int) Returns the font's current wrap alignment option.

## Remarks

The wrap alignment option can be one of the following:

- [`TTF_WRAPPED_ALIGN_LEFT`](TTF_WRAPPED_ALIGN_LEFT)
- [`TTF_WRAPPED_ALIGN_CENTER`](TTF_WRAPPED_ALIGN_CENTER)
- [`TTF_WRAPPED_ALIGN_RIGHT`](TTF_WRAPPED_ALIGN_RIGHT)

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontWrappedAlign](TTF_SetFontWrappedAlign)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

