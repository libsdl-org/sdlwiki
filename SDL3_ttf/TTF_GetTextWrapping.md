###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextWrapping

Get whether wrapping is enabled on a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextWrapping(TTF_Text *text, bool *wrap, int *wrapLength);
```

## Function Parameters

|                        |                |                                                                                                                            |
| ---------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text**       | the [TTF_Text](TTF_Text) to query.                                                                                         |
| bool *                 | **wrap**       | a pointer filled in with true if wrapping is enabled, false if it is disabled, may be NULL.                                |
| int *                  | **wrapLength** | a pointer filled in with the maximum width in pixels or 0 if the text is being wrapped on newline characters, may be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

