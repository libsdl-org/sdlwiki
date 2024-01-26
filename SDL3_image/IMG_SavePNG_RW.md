###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SavePNG_RW

Save an SDL_Surface into PNG image data, via an SDL_RWops.

## Syntax

```c
int IMG_SavePNG_RW(SDL_Surface *surface, SDL_RWops *dst, int freedst);

```

## Function Parameters

|                 |                                                                                    |
| --------------- | ---------------------------------------------------------------------------------- |
| **surface**     | the SDL surface to save                                                            |
| **dst**         | the SDL_RWops to save the image data to.                                           |
| **freedst**     | SDL_TRUE to close/free the SDL_RWops before returning, SDL_FALSE to leave it open. |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

If you just want to save to a filename, you can use
[IMG_SavePNG](IMG_SavePNG)() instead.

If `freedst` is SDL_TRUE, the RWops will be closed before returning,
whether this function succeeds or not.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_SavePNG](IMG_SavePNG)

----
[CategoryAPI](CategoryAPI)

