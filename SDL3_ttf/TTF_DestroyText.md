###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_DestroyText

Destroy a text object created by a text engine.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_DestroyText(TTF_Text *text);
```

## Function Parameters

|                        |          |                      |
| ---------------------- | -------- | -------------------- |
| [TTF_Text](TTF_Text) * | **text** | the text to destroy. |

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CreateText](TTF_CreateText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

