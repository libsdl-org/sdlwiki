###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextDirection

Set the direction to be used for text shaping a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextDirection(TTF_Text *text, TTF_Direction direction);
```

## Function Parameters

|                                |               |                                     |
| ------------------------------ | ------------- | ----------------------------------- |
| [TTF_Text](TTF_Text) *         | **text**      | the text to modify.                 |
| [TTF_Direction](TTF_Direction) | **direction** | the new direction for text to flow. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This function only supports left-to-right text shaping if SDL_ttf was not
built with HarfBuzz support.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

