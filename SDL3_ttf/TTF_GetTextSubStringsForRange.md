###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextSubStringsForRange

Get the substrings of a text object that contain a range of text.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_SubString ** TTF_GetTextSubStringsForRange(TTF_Text *text, int offset, int length, int *count);
```

## Function Parameters

|                        |            |                                                                                         |
| ---------------------- | ---------- | --------------------------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text**   | the [TTF_Text](TTF_Text) to query.                                                      |
| int                    | **offset** | a byte offset into the text string.                                                     |
| int                    | **length** | the length of the range being queried, in bytes, or -1 for the remainder of the string. |
| int *                  | **count**  | a pointer filled in with the number of substrings returned, may be NULL.                |

## Return Value

([TTF_SubString](TTF_SubString) **) Returns a NULL terminated array of
substring pointers or NULL on failure; call SDL_GetError() for more
information. This is a single allocation that should be freed with
SDL_free() when it is no longer needed.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

