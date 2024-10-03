###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextSubStringsForRange

Get the substrings of a text object that contain a range of text.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_SubString ** TTF_GetTextSubStringsForRange(TTF_Text *text, int offset1, int offset2, int *count);
```

## Function Parameters

|                        |             |                                                                          |
| ---------------------- | ----------- | ------------------------------------------------------------------------ |
| [TTF_Text](TTF_Text) * | **text**    | the [TTF_Text](TTF_Text) to query.                                       |
| int                    | **offset1** | the first byte offset into the text string.                              |
| int                    | **offset2** | the second byte offset into the text string.                             |
| int *                  | **count**   | a pointer filled in with the number of substrings returned, may be NULL. |

## Return Value

([TTF_SubString](TTF_SubString) **) Returns a NULL terminated array of
substring pointers or NULL on failure; call SDL_GetError() for more
information. This is a single allocation that should be freed with
SDL_free() when it is no longer needed.

## Remarks

The smaller offset will be clamped to 0 and the larger offset will be
clamped to the length of text minus 1. The substrings that are returned
will include the first offset and the second offset inclusive, e.g. {0, 2}
of "abcd" will return "abc". If the text is empty, this will return a
single zero width substring.

If an offset is negative, it will be considered as an offset from the end
of the text, so {0, -1} would return substrings for the entire text.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

