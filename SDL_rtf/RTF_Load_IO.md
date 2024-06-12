###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_Load_IO

Set the text of an RTF context, with data loaded from an SDL_IOStream.

## Header File

Defined in [<SDL3_rtf/SDL_rtf.h>](https://github.com/libsdl-org/SDL_rtf/blob/main/include/SDL3_rtf/SDL_rtf.h)

## Syntax

```c
int RTF_Load_IO(RTF_Context *ctx, SDL_IOStream *src, int closeio);
```

## Function Parameters

|                              |             |                                                   |
| ---------------------------- | ----------- | ------------------------------------------------- |
| [RTF_Context](RTF_Context) * | **ctx**     | the RTF context to update.                        |
| SDL_IOStream *               | **src**     | the SDL_IOStream to load RTF data from.           |
| int                          | **closeio** | non-zero to close/free `src`, zero to leave open. |

## Return Value

(int) Returns 0 on success, -1 on failure.

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

