###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveAVIF_IO

Save an SDL_Surface into AVIF image data, via an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
int IMG_SaveAVIF_IO(SDL_Surface *surface, SDL_IOStream *dst, int closeio, int quality);
```

## Function Parameters

|                |             |                                                                                       |
| -------------- | ----------- | ------------------------------------------------------------------------------------- |
| SDL_Surface *  | **surface** | the SDL surface to save                                                               |
| SDL_IOStream * | **dst**     | the SDL_IOStream to save the image data to.                                           |
| int            | **closeio** | SDL_TRUE to close/free the SDL_IOStream before returning, SDL_FALSE to leave it open. |
| int            | **quality** | the desired quality, ranging between 0 (lowest) and 100 (highest)                     |

## Return Value

(int) Returns 0 if successful, -1 on error.

## Remarks

If you just want to save to a filename, you can use
[IMG_SaveAVIF](IMG_SaveAVIF)() instead.

If `closeio` is SDL_TRUE, `dst` will be closed before returning, whether
this function succeeds or not.

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_SaveAVIF](IMG_SaveAVIF)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

