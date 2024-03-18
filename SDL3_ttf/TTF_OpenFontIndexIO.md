###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_OpenFontIndexIO

Create a font from an SDL_IOStream, using a specified face index.

## Syntax

```c
TTF_Font * TTF_OpenFontIndexIO(SDL_IOStream *src, SDL_bool closeio, int ptsize, long index);

```

## Function Parameters

|                 |                                                                              |
| --------------- | ---------------------------------------------------------------------------- |
| **src**         | an SDL_IOStream to provide a font file's data.                               |
| **closeio**     | SDL_TRUE to close `src` when the font is closed, SDL_FALSE to leave it open. |
| **ptsize**      | point size to use for the newly-opened font.                                 |
| **index**       | index of the face in the font file.                                          |

## Return Value

Returns a valid [TTF_Font](TTF_Font), or NULL on error.

## Remarks

Some .fon fonts will have several sizes embedded in the file, so the point
size becomes the index of choosing which size. If the value is too high,
the last indexed size will be the default.

If `closeio` is SDL_TRUE `src` will be automatically closed once the font
is closed. Otherwise you should close `src` yourself after closing the
font.

Some fonts have multiple "faces" included. The index specifies which face
to use from the font file. Font files with only one face should specify
zero for the index.

When done with the returned [TTF_Font](TTF_Font), use
[TTF_CloseFont](TTF_CloseFont)() to dispose of it.

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_CloseFont](TTF_CloseFont)

----
[CategoryAPI](CategoryAPI)

