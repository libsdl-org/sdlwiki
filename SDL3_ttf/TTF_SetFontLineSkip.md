###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontLineSkip

Set the spacing between lines of text for a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_SetFontLineSkip(TTF_Font *font, int lineskip);
```

## Function Parameters

|                        |              |                                    |
| ---------------------- | ------------ | ---------------------------------- |
| [TTF_Font](TTF_Font) * | **font**     | the font to modify.                |
| int                    | **lineskip** | the new line spacing for the font. |

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

