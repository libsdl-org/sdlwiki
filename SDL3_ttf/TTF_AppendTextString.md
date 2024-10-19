###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_AppendTextString

Append UTF-8 text to a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_AppendTextString(TTF_Text *text, const char *string, size_t length);
```

## Function Parameters

|                        |            |                                                                  |
| ---------------------- | ---------- | ---------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text**   | the [TTF_Text](TTF_Text) to modify.                              |
| const char *           | **string** | the UTF-8 text to insert.                                        |
| size_t                 | **length** | the length of the text, in bytes, or 0 for null terminated text. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

