###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadICO_IO

Load a ICO image directly.

## Syntax

```c
SDL_Surface * IMG_LoadICO_IO(SDL_IOStream *src);

```

## Function Parameters

|             |                                          |
| ----------- | ---------------------------------------- |
| **src**     | an SDL_IOStream to load image data from. |

## Return Value

Returns SDL surface, or NULL on error

## Remarks

If you know you definitely have a ICO image, you can call this function,
which will skip SDL_image's file format detection routines. Generally it's
better to use the abstract interfaces; also, there is only an SDL_IOStream
interface available here.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_LoadAVIF_IO](IMG_LoadAVIF_IO)
* [IMG_LoadCUR_IO](IMG_LoadCUR_IO)
* [IMG_LoadBMP_IO](IMG_LoadBMP_IO)
* [IMG_LoadGIF_IO](IMG_LoadGIF_IO)
* [IMG_LoadJPG_IO](IMG_LoadJPG_IO)
* [IMG_LoadJXL_IO](IMG_LoadJXL_IO)
* [IMG_LoadLBM_IO](IMG_LoadLBM_IO)
* [IMG_LoadPCX_IO](IMG_LoadPCX_IO)
* [IMG_LoadPNG_IO](IMG_LoadPNG_IO)
* [IMG_LoadPNM_IO](IMG_LoadPNM_IO)
* [IMG_LoadSVG_IO](IMG_LoadSVG_IO)
* [IMG_LoadQOI_IO](IMG_LoadQOI_IO)
* [IMG_LoadTGA_IO](IMG_LoadTGA_IO)
* [IMG_LoadTIF_IO](IMG_LoadTIF_IO)
* [IMG_LoadXCF_IO](IMG_LoadXCF_IO)
* [IMG_LoadXPM_IO](IMG_LoadXPM_IO)
* [IMG_LoadXV_IO](IMG_LoadXV_IO)
* [IMG_LoadWEBP_IO](IMG_LoadWEBP_IO)

----
[CategoryAPI](CategoryAPI)

