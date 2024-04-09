###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_FontDescent

Query the offset from the baseline to the bottom of a font.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
int TTF_FontDescent(const TTF_Font *font);

```

## Function Parameters

|              |                    |
| ------------ | ------------------ |
| **font**     | the font to query. |

## Return Value

Returns the font's descent.

## Remarks

This is a negative value, relative to the baseline.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

