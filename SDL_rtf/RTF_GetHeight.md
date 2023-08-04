###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_GetHeight

Get the height of an RTF render area given a certain width.

## Syntax

```c
int RTF_GetHeight(RTF_Context *ctx, int width);

```

## Function Parameters

|               |                                             |
| ------------- | ------------------------------------------- |
| **ctx**       | the RTF context to query.                   |
| **width**     | the width, in pixels, to use for text flow. |

## Return Value

Returns the height, in pixels, of an RTF render area.

## Remarks

The text is automatically reflowed to this new width, and should match the
width of the clipping rectangle used for rendering later.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI)

