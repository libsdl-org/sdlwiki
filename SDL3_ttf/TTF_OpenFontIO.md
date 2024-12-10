###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_OpenFontIO

Create a font from an SDL_IOStream, using a specified point size.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_Font * TTF_OpenFontIO(SDL_IOStream *src, bool closeio, float ptsize);
```

## Function Parameters

|                |             |                                                                      |
| -------------- | ----------- | -------------------------------------------------------------------- |
| SDL_IOStream * | **src**     | an SDL_IOStream to provide a font file's data.                       |
| bool           | **closeio** | true to close `src` when the font is closed, false to leave it open. |
| float          | **ptsize**  | point size to use for the newly-opened font.                         |

## Return Value

([TTF_Font](TTF_Font) *) Returns a valid [TTF_Font](TTF_Font), or NULL on
failure; call SDL_GetError() for more information.

## Remarks

Some .fon fonts will have several sizes embedded in the file, so the point
size becomes the index of choosing which size. If the value is too high,
the last indexed size will be the default.

If `closeio` is true, `src` will be automatically closed once the font is
closed. Otherwise you should close `src` yourself after closing the font.

When done with the returned [TTF_Font](TTF_Font), use
[TTF_CloseFont](TTF_CloseFont)() to dispose of it.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CloseFont](TTF_CloseFont)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

