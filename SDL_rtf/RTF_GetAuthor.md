###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_GetAuthor

Get the author of an RTF document.

## Header File

Defined in [<SDL3_rtf/SDL_rtf.h>](https://github.com/libsdl-org/SDL_rtf/blob/main/include/SDL3_rtf/SDL_rtf.h)

## Syntax

```c
const char * RTF_GetAuthor(RTF_Context *ctx);
```

## Function Parameters

|                              |         |                           |
| ---------------------------- | ------- | ------------------------- |
| [RTF_Context](RTF_Context) * | **ctx** | the RTF context to query. |

## Return Value

(const char *) Returns the document author in UTF-8 encoding.

## Remarks

The returned string is part of the [RTF_Context](RTF_Context), and should
not be modified or freed by the application. The pointer remains valid
until the [RTF_Context](RTF_Context) is freed.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

