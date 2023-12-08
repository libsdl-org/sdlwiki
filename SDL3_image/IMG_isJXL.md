###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_isJXL

Detect JXL image data on a readable/seekable SDL_RWops.

## Syntax

```c
int IMG_isJXL(SDL_RWops *src);

```

## Function Parameters

|             |                                                      |
| ----------- | ---------------------------------------------------- |
| **src**     | a seekable/readable SDL_RWops to provide image data. |

## Return Value

Returns non-zero if this is JXL data, zero otherwise.

## Remarks

This function attempts to determine if a file is a given filetype, reading
the least amount possible from the SDL_RWops (usually a few bytes).

There is no distinction made between "not the filetype in question" and
basic i/o errors.

This function will always attempt to seek the RWops back to where it
started when this function was called, but it will not report any errors in
doing so, but assuming seeking works, this means you can immediately use
this with a different [IMG_isTYPE](IMG_isTYPE.md) function, or load the image
without further seeking.

You do not need to call this function to load data; SDL_image can work to
determine file type in many cases in its standard load functions.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_isAVIF](IMG_isAVIF.md)
* [IMG_isICO](IMG_isICO.md)
* [IMG_isCUR](IMG_isCUR.md)
* [IMG_isBMP](IMG_isBMP.md)
* [IMG_isGIF](IMG_isGIF.md)
* [IMG_isJPG](IMG_isJPG.md)
* [IMG_isLBM](IMG_isLBM.md)
* [IMG_isPCX](IMG_isPCX.md)
* [IMG_isPNG](IMG_isPNG.md)
* [IMG_isPNM](IMG_isPNM.md)
* [IMG_isSVG](IMG_isSVG.md)
* [IMG_isQOI](IMG_isQOI.md)
* [IMG_isTIF](IMG_isTIF.md)
* [IMG_isXCF](IMG_isXCF.md)
* [IMG_isXPM](IMG_isXPM.md)
* [IMG_isXV](IMG_isXV.md)
* [IMG_isWEBP](IMG_isWEBP.md)

----
[CategoryAPI](CategoryAPI.md)
