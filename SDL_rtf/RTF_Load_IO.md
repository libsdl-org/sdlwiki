###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_Load_IO

Set the text of an RTF context, with data loaded from an SDL_IOStream.

## Header File

Defined in [<SDL3_rtf/SDL_rtf.h>](https://github.com/libsdl-org/SDL_rtf/blob/main/include/SDL3_rtf/SDL_rtf.h)

## Syntax

```c
bool RTF_Load_IO(RTF_Context *ctx, SDL_IOStream *src, bool closeio);
```

## Function Parameters

|                              |             |                                                                      |
| ---------------------------- | ----------- | -------------------------------------------------------------------- |
| [RTF_Context](RTF_Context) * | **ctx**     | the RTF context to update.                                           |
| SDL_IOStream *               | **src**     | the SDL_IOStream to load RTF data from.                              |
| bool                         | **closeio** | true to close `src` when the font is closed, false to leave it open. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This can be called multiple times to change the text displayed.

If `closeio` is true, this function will close `src`, whether this function
succeeded or not.

On failure, call [RTF_GetError](RTF_GetError)() to get a human-readable
text message corresponding to the error.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

