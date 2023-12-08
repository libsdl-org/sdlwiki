###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_GetTitle

Get the title of an RTF document.

## Syntax

```c
const char * RTF_GetTitle(RTF_Context *ctx);

```

## Function Parameters

|             |                           |
| ----------- | ------------------------- |
| **ctx**     | the RTF context to query. |

## Return Value

Returns the document title in UTF-8 encoding.

## Remarks

The returned string is part of the [RTF_Context](RTF_Context.md), and should
not be modified or freed by the application. The pointer remains valid
until the [RTF_Context](RTF_Context.md) is freed.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
