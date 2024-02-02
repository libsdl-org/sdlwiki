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

For HDR images, the returned surface may have light information properties:

- `SDL_PROP_SURFACE_MAXCLL_NUMBER`: MaxCLL (Maximum Content Light Level)
  indicates the maximum light level of any single pixel (in cd/m2 or nits)
  of the entire playback sequence. MaxCLL is usually measured off the final
  delivered content after mastering. If one uses the full light level of
  the HDR mastering display and adds a hard clip at its maximum value,
  MaxCLL would be equal to the peak luminance of the mastering monitor.
- `SDL_PROP_SURFACE_MAXFALL_NUMBER`: MaxFALL (Maximum Frame Average Light
  Level) indicates the maximum value of the frame average light level (in
  cd/m2 or nits) of the entire playback sequence. MaxFALL is calculated by
  averaging the decoded luminance values of all the pixels within a frame.
  MaxFALL is usually much lower than MaxCLL.

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

