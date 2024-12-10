###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SubStringFlags

Flags for [TTF_SubString](TTF_SubString)

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef Uint32 TTF_SubStringFlags;

#define TTF_SUBSTRING_TEXT_START    0x00000001  /**< This substring contains the beginning of the text */
#define TTF_SUBSTRING_LINE_START    0x00000002  /**< This substring contains the beginning of line `line_index` */
#define TTF_SUBSTRING_LINE_END      0x00000004  /**< This substring contains the end of line `line_index` */
#define TTF_SUBSTRING_TEXT_END      0x00000008  /**< This substring contains the end of the text */
```

## Version

This datatype is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SubString](TTF_SubString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLTTF](CategorySDLTTF)

