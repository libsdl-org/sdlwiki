###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_OpenFontWithProperties

Create a font with the specified properties.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_Font * TTF_OpenFontWithProperties(SDL_PropertiesID props);


#define TTF_PROP_FONT_CREATE_FILENAME_STRING            "SDL_ttf.font.create.filename"
#define TTF_PROP_FONT_CREATE_IOSTREAM_POINTER           "SDL_ttf.font.create.iostream"
#define TTF_PROP_FONT_CREATE_IOSTREAM_OFFSET_NUMBER     "SDL_ttf.font.create.iostream.offset"
#define TTF_PROP_FONT_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN "SDL_ttf.font.create.iostream.autoclose"
#define TTF_PROP_FONT_CREATE_SIZE_FLOAT                 "SDL_ttf.font.create.size"
#define TTF_PROP_FONT_CREATE_FACE_NUMBER                "SDL_ttf.font.create.face"
#define TTF_PROP_FONT_CREATE_HORIZONTAL_DPI_NUMBER      "SDL_ttf.font.create.hdpi"
#define TTF_PROP_FONT_CREATE_VERTICAL_DPI_NUMBER        "SDL_ttf.font.create.vdpi"
```

## Function Parameters

|                  |           |                        |
| ---------------- | --------- | ---------------------- |
| SDL_PropertiesID | **props** | the properties to use. |

## Return Value

([TTF_Font](TTF_Font) *) Returns a valid [TTF_Font](TTF_Font), or NULL on
failure; call SDL_GetError() for more information.

## Remarks

These are the supported properties:

- [`TTF_PROP_FONT_CREATE_FILENAME_STRING`](TTF_PROP_FONT_CREATE_FILENAME_STRING):
  the font file to open, if an SDL_IOStream isn't being used. This is
  required if
  [`TTF_PROP_FONT_CREATE_IOSTREAM_POINTER`](TTF_PROP_FONT_CREATE_IOSTREAM_POINTER)
  isn't set.
- [`TTF_PROP_FONT_CREATE_IOSTREAM_POINTER`](TTF_PROP_FONT_CREATE_IOSTREAM_POINTER):
  an SDL_IOStream containing the font to be opened. This should not be
  closed until the font is closed. This is required if
  [`TTF_PROP_FONT_CREATE_FILENAME_STRING`](TTF_PROP_FONT_CREATE_FILENAME_STRING)
  isn't set.
- [`TTF_PROP_FONT_CREATE_IOSTREAM_OFFSET_NUMBER`](TTF_PROP_FONT_CREATE_IOSTREAM_OFFSET_NUMBER):
  the offset in the iostream for the beginning of the font, defaults to 0.
- [`TTF_PROP_FONT_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN`](TTF_PROP_FONT_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN):
  true if closing the font should also close the associated SDL_IOStream.
- [`TTF_PROP_FONT_CREATE_SIZE_NUMBER`](TTF_PROP_FONT_CREATE_SIZE_NUMBER):
  the point size of the font. Some .fon fonts will have several sizes
  embedded in the file, so the point size becomes the index of choosing
  which size. If the value is too high, the last indexed size will be the
  default.
- [`TTF_PROP_FONT_CREATE_FACE_NUMBER`](TTF_PROP_FONT_CREATE_FACE_NUMBER):
  the face index of the font, if the font contains multiple font faces.
- [`TTF_PROP_FONT_CREATE_HORIZONTAL_DPI_NUMBER`](TTF_PROP_FONT_CREATE_HORIZONTAL_DPI_NUMBER):
  the horizontal DPI to use for font rendering, defaults to
  [`TTF_PROP_FONT_CREATE_VERTICAL_DPI_NUMBER`](TTF_PROP_FONT_CREATE_VERTICAL_DPI_NUMBER)
  if set, or 72 otherwise.
- [`TTF_PROP_FONT_CREATE_VERTICAL_DPI_NUMBER`](TTF_PROP_FONT_CREATE_VERTICAL_DPI_NUMBER):
  the vertical DPI to use for font rendering, defaults to
  [`TTF_PROP_FONT_CREATE_HORIZONTAL_DPI_NUMBER`](TTF_PROP_FONT_CREATE_HORIZONTAL_DPI_NUMBER)
  if set, or 72 otherwise.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CloseFont](TTF_CloseFont)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

