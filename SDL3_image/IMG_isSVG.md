###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_isSVG

Detect SVG image data on a readable/seekable SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
int IMG_isSVG(SDL_IOStream *src);
```

## Function Parameters

|                |         |                                                         |
| -------------- | ------- | ------------------------------------------------------- |
| SDL_IOStream * | **src** | a seekable/readable SDL_IOStream to provide image data. |

## Return Value

(int) Returns non-zero if this is SVG data, zero otherwise.

## Remarks

This function attempts to determine if a file is a given filetype, reading
the least amount possible from the SDL_IOStream (usually a few bytes).

There is no distinction made between "not the filetype in question" and
basic i/o errors.

This function will always attempt to seek `src` back to where it started
when this function was called, but it will not report any errors in doing
so, but assuming seeking works, this means you can immediately use this
with a different [IMG_isTYPE](IMG_isTYPE) function, or load the image
without further seeking.

You do not need to call this function to load data; SDL_image can work to
determine file type in many cases in its standard load functions.

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_isAVIF](IMG_isAVIF)
- [IMG_isICO](IMG_isICO)
- [IMG_isCUR](IMG_isCUR)
- [IMG_isBMP](IMG_isBMP)
- [IMG_isGIF](IMG_isGIF)
- [IMG_isJPG](IMG_isJPG)
- [IMG_isJXL](IMG_isJXL)
- [IMG_isLBM](IMG_isLBM)
- [IMG_isPCX](IMG_isPCX)
- [IMG_isPNG](IMG_isPNG)
- [IMG_isPNM](IMG_isPNM)
- [IMG_isQOI](IMG_isQOI)
- [IMG_isTIF](IMG_isTIF)
- [IMG_isXCF](IMG_isXCF)
- [IMG_isXPM](IMG_isXPM)
- [IMG_isXV](IMG_isXV)
- [IMG_isWEBP](IMG_isWEBP)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

