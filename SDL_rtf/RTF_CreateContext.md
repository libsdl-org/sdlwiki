###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_CreateContext

Create an RTF display context, with the given font engine.

## Syntax

```c
RTF_Context * RTF_CreateContext(SDL_Renderer *renderer, RTF_FontEngine *fontEngine);

```

## Function Parameters

|                    |                                            |
| ------------------ | ------------------------------------------ |
| **renderer**       | an SDL renderer to use for drawing.        |
| **fontEngine**     | the font engine to use for rendering text. |

## Return Value

Returns a new RTF display context, or NULL on error.

## Remarks

Once a context is created, it can be used to load and display text in
Microsoft RTF format.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
