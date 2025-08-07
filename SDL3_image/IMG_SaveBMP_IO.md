###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveBMP_IO

Save an SDL_Surface into BMP image data, via an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_SaveBMP_IO(SDL_Surface *surface, SDL_IOStream *dst, bool closeio);
```

## Function Parameters

|                |             |                                                                               |
| -------------- | ----------- | ----------------------------------------------------------------------------- |
| SDL_Surface *  | **surface** | the SDL surface to save.                                                      |
| SDL_IOStream * | **dst**     | the SDL_IOStream to save the image data to.                                   |
| bool           | **closeio** | true to close/free the SDL_IOStream before returning, false to leave it open. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If you just want to save to a filename, you can use
[IMG_SaveBMP](IMG_SaveBMP)() instead.

If `closeio` is true, `dst` will be closed before returning, whether this
function succeeds or not.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_SaveBMP](IMG_SaveBMP)
- [IMG_SaveAVIF_IO](IMG_SaveAVIF_IO)
- [IMG_SaveGIF_IO](IMG_SaveGIF_IO)
- [IMG_SaveJPG_IO](IMG_SaveJPG_IO)
- [IMG_SavePNG_IO](IMG_SavePNG_IO)
- [IMG_SaveTGA_IO](IMG_SaveTGA_IO)
- [IMG_SaveWEBP_IO](IMG_SaveWEBP_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

