###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_CreateContext

Create an RTF display context, with the given font engine.

## Header File

Defined in [<SDL3_rtf/SDL_rtf.h>](https://github.com/libsdl-org/SDL_rtf/blob/main/include/SDL3_rtf/SDL_rtf.h)

## Syntax

```c
RTF_Context * RTF_CreateContext(SDL_Renderer *renderer, RTF_FontEngine *fontEngine);
```

## Function Parameters

|                                    |                |                                            |
| ---------------------------------- | -------------- | ------------------------------------------ |
| SDL_Renderer *                     | **renderer**   | an SDL renderer to use for drawing.        |
| [RTF_FontEngine](RTF_FontEngine) * | **fontEngine** | the font engine to use for rendering text. |

## Return Value

([RTF_Context](RTF_Context) *) Returns a new RTF display context, or NULL
on error.

## Remarks

Once a context is created, it can be used to load and display text in
Microsoft RTF format.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

