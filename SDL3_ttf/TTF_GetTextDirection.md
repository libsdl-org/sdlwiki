###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextDirection

Get the direction to be used for text shaping a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_Direction TTF_GetTextDirection(TTF_Text *text);
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Text](TTF_Text) * | **text** | the text to query. |

## Return Value

([TTF_Direction](TTF_Direction)) Returns the direction to be used for text
shaping.

## Remarks

This defaults to the direction of the font used by the text object.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

