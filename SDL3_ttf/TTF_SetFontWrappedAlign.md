###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontWrappedAlign

Set a font's current wrap alignment option.

## Syntax

```c
void TTF_SetFontWrappedAlign(TTF_Font *font, int align);

```

## Function Parameters

|               |                                                 |
| ------------- | ----------------------------------------------- |
| **font**      | the font to set a new wrap alignment option on. |
| **align**     | the new wrap alignment option.                  |

## Remarks

The wrap alignment option can be one of the following:

- [`TTF_WRAPPED_ALIGN_LEFT`](TTF_WRAPPED_ALIGN_LEFT)
- [`TTF_WRAPPED_ALIGN_CENTER`](TTF_WRAPPED_ALIGN_CENTER)
- [`TTF_WRAPPED_ALIGN_RIGHT`](TTF_WRAPPED_ALIGN_RIGHT)

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_GetFontWrappedAlign](TTF_GetFontWrappedAlign)

----
[CategoryAPI](CategoryAPI)

