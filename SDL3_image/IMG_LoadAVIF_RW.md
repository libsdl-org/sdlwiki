###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadAVIF_RW

Load a AVIF image directly.

## Syntax

```c
SDL_Surface * IMG_LoadAVIF_RW(SDL_RWops *src);

```

## Function Parameters

|             |                                       |
| ----------- | ------------------------------------- |
| **src**     | an SDL_RWops to load image data from. |

## Return Value

Returns SDL surface, or NULL on error

## Remarks

If you know you definitely have a AVIF image, you can call this function,
which will skip SDL_image's file format detection routines. Generally it's
better to use the abstract interfaces; also, there is only an SDL_RWops
interface available here.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_LoadICO_RW](IMG_LoadICO_RW)
* [IMG_LoadCUR_RW](IMG_LoadCUR_RW)
* [IMG_LoadBMP_RW](IMG_LoadBMP_RW)
* [IMG_LoadGIF_RW](IMG_LoadGIF_RW)
* [IMG_LoadJPG_RW](IMG_LoadJPG_RW)
* [IMG_LoadJXL_RW](IMG_LoadJXL_RW)
* [IMG_LoadLBM_RW](IMG_LoadLBM_RW)
* [IMG_LoadPCX_RW](IMG_LoadPCX_RW)
* [IMG_LoadPNG_RW](IMG_LoadPNG_RW)
* [IMG_LoadPNM_RW](IMG_LoadPNM_RW)
* [IMG_LoadSVG_RW](IMG_LoadSVG_RW)
* [IMG_LoadQOI_RW](IMG_LoadQOI_RW)
* [IMG_LoadTGA_RW](IMG_LoadTGA_RW)
* [IMG_LoadTIF_RW](IMG_LoadTIF_RW)
* [IMG_LoadXCF_RW](IMG_LoadXCF_RW)
* [IMG_LoadXPM_RW](IMG_LoadXPM_RW)
* [IMG_LoadXV_RW](IMG_LoadXV_RW)
* [IMG_LoadWEBP_RW](IMG_LoadWEBP_RW)

----
[CategoryAPI](CategoryAPI)

