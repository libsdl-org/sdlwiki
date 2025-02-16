###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontSDF

Query whether Signed Distance Field rendering is enabled for a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetFontSDF(const TTF_Font *font);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(bool) Returns true if enabled, false otherwise.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontSDF](TTF_SetFontSDF)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

