###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveBMP

Save an SDL_Surface into a BMP image file.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_SaveBMP(SDL_Surface *surface, const char *file);
```

## Function Parameters

|               |             |                                              |
| ------------- | ----------- | -------------------------------------------- |
| SDL_Surface * | **surface** | the SDL surface to save.                     |
| const char *  | **file**    | path on the filesystem to write new file to. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If the file already exists, it will be overwritten.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_SaveBMP_IO](IMG_SaveBMP_IO)
- [IMG_SaveAVIF](IMG_SaveAVIF)
- [IMG_SaveGIF](IMG_SaveGIF)
- [IMG_SaveJPG](IMG_SaveJPG)
- [IMG_SavePNG](IMG_SavePNG)
- [IMG_SaveTGA](IMG_SaveTGA)
- [IMG_SaveWEBP](IMG_SaveWEBP)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

