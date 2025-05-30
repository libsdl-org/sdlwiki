###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontScript

Get the script used for text shaping a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
Uint32 TTF_GetFontScript(TTF_Font *font);
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(Uint32) Returns an
[ISO 15924 code](https://unicode.org/iso15924/iso15924-codes.html)
or 0 if a script hasn't been set.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_TagToString](TTF_TagToString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

