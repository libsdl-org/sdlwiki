###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontScriptName

Set script to be used for text shaping by a font.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
int TTF_SetFontScriptName(TTF_Font *font, const char *script);

```

## Function Parameters

|                |                                                 |
| -------------- | ----------------------------------------------- |
| **font**       | the font to specify a direction for.            |
| **script**     | null-terminated string of exactly 4 characters. |

## Return Value

Returns 0 on success, or -1 on error.

## Remarks

The supplied script value must be a null-terminated string of exactly four
characters.

If SDL_ttf was not built with HarfBuzz support, this function returns -1.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

