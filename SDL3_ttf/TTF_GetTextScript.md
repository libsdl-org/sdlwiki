###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextScript

Get the script used for text shaping a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
Uint32 TTF_GetTextScript(TTF_Text *text);
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Text](TTF_Text) * | **text** | the text to query. |

## Return Value

(Uint32) Returns an
[ISO 15924 code](https://unicode.org/iso15924/iso15924-codes.html)
or 0 if a script hasn't been set on either the text object or the font.

## Remarks

This defaults to the script of the font used by the text object.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_TagToString](TTF_TagToString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

