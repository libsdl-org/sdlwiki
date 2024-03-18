###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_isBMP

Detect BMP image data on a readable/seekable SDL_IOStream.

## Syntax

```c
int IMG_isBMP(SDL_IOStream *src);

```

## Function Parameters

|             |                                                         |
| ----------- | ------------------------------------------------------- |
| **src**     | a seekable/readable SDL_IOStream to provide image data. |

## Return Value

Returns non-zero if this is BMP data, zero otherwise.

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

## Related Functions

* [IMG_isAVIF](IMG_isAVIF)
* [IMG_isICO](IMG_isICO)
* [IMG_isCUR](IMG_isCUR)
* [IMG_isGIF](IMG_isGIF)
* [IMG_isJPG](IMG_isJPG)
* [IMG_isJXL](IMG_isJXL)
* [IMG_isLBM](IMG_isLBM)
* [IMG_isPCX](IMG_isPCX)
* [IMG_isPNG](IMG_isPNG)
* [IMG_isPNM](IMG_isPNM)
* [IMG_isSVG](IMG_isSVG)
* [IMG_isQOI](IMG_isQOI)
* [IMG_isTIF](IMG_isTIF)
* [IMG_isXCF](IMG_isXCF)
* [IMG_isXPM](IMG_isXPM)
* [IMG_isXV](IMG_isXV)
* [IMG_isWEBP](IMG_isWEBP)

----
[CategoryAPI](CategoryAPI)

