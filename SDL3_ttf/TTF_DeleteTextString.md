###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_DeleteTextString

Delete UTF-8 text from a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_DeleteTextString(TTF_Text *text, int offset, int length);
```

## Function Parameters

|                        |            |                                                                                                                                                                                                                    |
| ---------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [TTF_Text](TTF_Text) * | **text**   | the [TTF_Text](TTF_Text) to modify.                                                                                                                                                                                |
| int                    | **offset** | the offset, in bytes, from the beginning of the string if >= 0, the offset from the end of the string if < 0. Note that this does not do UTF-8 validation, so you should only delete at UTF-8 sequence boundaries. |
| int                    | **length** | the length of text to delete, in bytes, or -1 for the remainder of the string.                                                                                                                                     |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

