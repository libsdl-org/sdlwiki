###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontGeneration

Get the font generation.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
Uint32 TTF_GetFontGeneration(TTF_Font *font);
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(Uint32) Returns the font generation or 0 on failure; call SDL_GetError()
for more information.

## Remarks

The generation is incremented each time font properties change that require
rebuilding glyphs, such as style, size, etc.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

