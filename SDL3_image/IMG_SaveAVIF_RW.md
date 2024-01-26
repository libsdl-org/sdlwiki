###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveAVIF_RW

Save an SDL_Surface into AVIF image data, via an SDL_RWops.

## Syntax

```c
int IMG_SaveAVIF_RW(SDL_Surface *surface, SDL_RWops *dst, int freedst, int quality);

```

## Function Parameters

|                 |                                                                                    |
| --------------- | ---------------------------------------------------------------------------------- |
| **surface**     | the SDL surface to save                                                            |
| **dst**         | the SDL_RWops to save the image data to.                                           |
| **freedst**     | SDL_TRUE to close/free the SDL_RWops before returning, SDL_FALSE to leave it open. |
| **quality**     | the desired quality, ranging between 0 (lowest) and 100 (highest)                  |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

If you just want to save to a filename, you can use
[IMG_SaveAVIF](IMG_SaveAVIF)() instead.

If `freedst` is SDL_TRUE, the RWops will be closed before returning,
whether this function succeeds or not.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_SaveAVIF](IMG_SaveAVIF)

----
[CategoryAPI](CategoryAPI)

