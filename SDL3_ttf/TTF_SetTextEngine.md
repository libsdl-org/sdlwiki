###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextEngine

Set the text engine used by a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextEngine(TTF_Text *text, TTF_TextEngine *engine);
```

## Function Parameters

|                                    |            |                                     |
| ---------------------------------- | ---------- | ----------------------------------- |
| [TTF_Text](TTF_Text) *             | **text**   | the [TTF_Text](TTF_Text) to modify. |
| [TTF_TextEngine](TTF_TextEngine) * | **engine** | the text engine to use for drawing. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

