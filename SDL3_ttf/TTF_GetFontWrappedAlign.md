###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontWrappedAlign

Query a font's current wrap alignment option.

## Syntax

```c
int TTF_GetFontWrappedAlign(const TTF_Font *font);

```

## Function Parameters

|              |                    |
| ------------ | ------------------ |
| **font**     | the font to query. |

## Return Value

Returns the font's current wrap alignment option.

## Remarks

The wrap alignment option can be one of the following:

- [`TTF_WRAPPED_ALIGN_LEFT`](TTF_WRAPPED_ALIGN_LEFT)
- [`TTF_WRAPPED_ALIGN_CENTER`](TTF_WRAPPED_ALIGN_CENTER)
- [`TTF_WRAPPED_ALIGN_RIGHT`](TTF_WRAPPED_ALIGN_RIGHT)

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_SetFontWrappedAlign](TTF_SetFontWrappedAlign.md)

----
[CategoryAPI](CategoryAPI.md)
