###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadPNG_RW

Load a PNG image directly.

## Syntax

```c
SDL_Surface * IMG_LoadPNG_RW(SDL_RWops *src);

```

## Function Parameters

|             |                                       |
| ----------- | ------------------------------------- |
| **src**     | an SDL_RWops to load image data from. |

## Return Value

Returns SDL surface, or NULL on error

## Remarks

If you know you definitely have a PNG image, you can call this function,
which will skip SDL_image's file format detection routines. Generally it's
better to use the abstract interfaces; also, there is only an SDL_RWops
interface available here.

## Version

This function is available since SDL_image 2.0.0.

## Related Functions

* [IMG_LoadAVIF_RW](IMG_LoadAVIF_RW.md)
* [IMG_LoadICO_RW](IMG_LoadICO_RW.md)
* [IMG_LoadCUR_RW](IMG_LoadCUR_RW.md)
* [IMG_LoadBMP_RW](IMG_LoadBMP_RW.md)
* [IMG_LoadGIF_RW](IMG_LoadGIF_RW.md)
* [IMG_LoadJPG_RW](IMG_LoadJPG_RW.md)
* [IMG_LoadJXL_RW](IMG_LoadJXL_RW.md)
* [IMG_LoadLBM_RW](IMG_LoadLBM_RW.md)
* [IMG_LoadPCX_RW](IMG_LoadPCX_RW.md)
* [IMG_LoadPNM_RW](IMG_LoadPNM_RW.md)
* [IMG_LoadSVG_RW](IMG_LoadSVG_RW.md)
* [IMG_LoadQOI_RW](IMG_LoadQOI_RW.md)
* [IMG_LoadTGA_RW](IMG_LoadTGA_RW.md)
* [IMG_LoadTIF_RW](IMG_LoadTIF_RW.md)
* [IMG_LoadXCF_RW](IMG_LoadXCF_RW.md)
* [IMG_LoadXPM_RW](IMG_LoadXPM_RW.md)
* [IMG_LoadXV_RW](IMG_LoadXV_RW.md)
* [IMG_LoadWEBP_RW](IMG_LoadWEBP_RW.md)

----
[CategoryAPI](CategoryAPI.md)
