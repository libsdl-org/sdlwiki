###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_Load_IO

Set the text of an RTF context, with data loaded from an SDL_IOStream.

## Header File

Defined in SDL_rtf.h

## Syntax

```c
int RTF_Load_IO(RTF_Context *ctx, SDL_IOStream *src, int closeio);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **ctx**         | the RTF context to update.                        |
| **src**         | the SDL_IOStream to load RTF data from.           |
| **closeio**     | non-zero to close/free `src`, zero to leave open. |

## Return Value

Returns 0 on success, -1 on failure.

## Remarks

This can be called multiple times to change the text displayed.

If `closeio` is non-zero, this function will close `src`, whether this
function succeeded or not.

On failure, call [RTF_GetError](RTF_GetError)() to get a human-readable
text message corresponding to the error.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

