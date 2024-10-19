###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CreateText

Create a text object from UTF-8 text and a text engine.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_Text * TTF_CreateText(TTF_TextEngine *engine, TTF_Font *font, const char *text, size_t length);
```

## Function Parameters

|                                    |            |                                                                    |
| ---------------------------------- | ---------- | ------------------------------------------------------------------ |
| [TTF_TextEngine](TTF_TextEngine) * | **engine** | the text engine to use when creating the text object, may be NULL. |
| [TTF_Font](TTF_Font) *             | **font**   | the font to render with.                                           |
| const char *                       | **text**   | the text to use, in UTF-8 encoding.                                |
| size_t                             | **length** | the length of the text, in bytes, or 0 for null terminated text.   |

## Return Value

([TTF_Text](TTF_Text) *) Returns a [TTF_Text](TTF_Text) object or NULL on
failure; call SDL_GetError() for more information.

## Remarks

This function is equivalent to `TTF_CreateText_Wrapped(engine, font, text,
0)` and will wrap on newline characters.

## Thread Safety

This function should be called on the thread that created the font and text
engine.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CreateText_Wrapped](TTF_CreateText_Wrapped)
- [TTF_DestroyText](TTF_DestroyText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

