###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_UpdateText

Update the layout of a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_UpdateText(TTF_Text *text);
```

## Function Parameters

|                        |          |                                     |
| ---------------------- | -------- | ----------------------------------- |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to update. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This is automatically done when the layout is requested or the text is
rendered, but you can call this if you need more control over the timing of
when the layout and text engine representation are updated.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

