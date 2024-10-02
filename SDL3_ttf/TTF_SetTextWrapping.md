###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextWrapping

Set whether wrapping is enabled on a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextWrapping(TTF_Text *text, bool wrap, int wrapLength);
```

## Function Parameters

|                        |                |                                                                                                    |
| ---------------------- | -------------- | -------------------------------------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text**       | the [TTF_Text](TTF_Text) to modify.                                                                |
| bool                   | **wrap**       | true if wrapping should be enabled, false if it should be disabled.                                |
| int                    | **wrapLength** | the maximum width in pixels, 0 to wrap on newline characters, or -1 to leave wrapLength unchanged. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

