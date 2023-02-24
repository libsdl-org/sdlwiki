###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_Render

Render the RTF document to a rectangle in an SDL_Renderer.

## Syntax

```c
void RTF_Render(RTF_Context *ctx, SDL_Rect *rect, int yOffset);

```

## Function Parameters

|                 |                                           |
| --------------- | ----------------------------------------- |
| **ctx**         | the RTF context render to.                |
| **rect**        | the area to render text into.             |
| **yOffset**     | offset up (and clip) by this many pixels. |

## Remarks

Rendering is done through the SDL_Renderer specified in
[RTF_CreateContext](RTF_CreateContext).

The text is reflowed to match the width of the rectangle.

The rendering is offset up (and clipped) by yOffset pixels.

## Version

This function is available since SDL_rtf 2.0.0.

----
[CategoryAPI](CategoryAPI)

