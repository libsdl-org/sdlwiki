###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_FreeContext

Free an RTF display context.

## Header File

Defined in [<SDL3_rtf/SDL_rtf.h>](https://github.com/libsdl-org/SDL_rtf/blob/main/include/SDL3_rtf/SDL_rtf.h)

## Syntax

```c
void RTF_FreeContext(RTF_Context *ctx);
```

## Function Parameters

|                              |         |                          |
| ---------------------------- | ------- | ------------------------ |
| [RTF_Context](RTF_Context) * | **ctx** | the RTF context to free. |

## Remarks

Call this when done rendering RTF content, to free resources used by this
context.

The context is not valid after this call. This does not destroy the
associated SDL_Renderer, which can continue to draw and present.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

