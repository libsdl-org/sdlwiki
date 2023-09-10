###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_OpenFontIndexDPI

Create a font from a file, using target resolutions (in DPI).

## Syntax

```c
TTF_Font * TTF_OpenFontIndexDPI(const char *file, int ptsize, long index, unsigned int hdpi, unsigned int vdpi);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **file**       | path to font file.                           |
| **ptsize**     | point size to use for the newly-opened font. |
| **index**      | index of the face in the font file.          |
| **hdpi**       | the target horizontal DPI.                   |
| **vdpi**       | the target vertical DPI.                     |

## Return Value

Returns a valid [TTF_Font](TTF_Font), or NULL on error.

## Remarks

DPI scaling only applies to scalable fonts (e.g. TrueType).

Some .fon fonts will have several sizes embedded in the file, so the point
size becomes the index of choosing which size. If the value is too high,
the last indexed size will be the default.

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

