###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextScript

Set the script to be used for text shaping a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextScript(TTF_Text *text, Uint32 script);
```

## Function Parameters

|                        |            |                                                                         |
| ---------------------- | ---------- | ----------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text**   | the text to modify.                                                     |
| Uint32                 | **script** | an [ISO 15924 code](https://unicode.org/iso15924/iso15924-codes.html) . |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This returns false if SDL_ttf isn't built with HarfBuzz support.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_StringToTag](TTF_StringToTag)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

