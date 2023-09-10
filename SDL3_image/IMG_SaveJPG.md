###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveJPG

Save an SDL_Surface into a JPEG image file.

## Syntax

```c
int IMG_SaveJPG(SDL_Surface *surface, const char *file, int quality);

```

## Function Parameters

|                 |                                                                                     |
| --------------- | ----------------------------------------------------------------------------------- |
| **surface**     | the SDL surface to save                                                             |
| **file**        | path on the filesystem to write new file to.                                        |
| **quality**     | [0; 33] is Lowest quality, [34; 66] is Middle quality, [67; 100] is Highest quality |

## Return Value

Returns 0 if successful, -1 on error

## Remarks

If the file already exists, it will be overwritten.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_SaveJPG_RW](IMG_SaveJPG_RW)
* [IMG_SavePNG](IMG_SavePNG)
* [IMG_SavePNG_RW](IMG_SavePNG_RW)

----
[CategoryAPI](CategoryAPI)

