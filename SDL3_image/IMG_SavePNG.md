###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SavePNG

Save an SDL_Surface into a PNG image file.

## Syntax

```c
int IMG_SavePNG(SDL_Surface *surface, const char *file);

```

## Function Parameters

|                 |                                              |
| --------------- | -------------------------------------------- |
| **surface**     | the SDL surface to save                      |
| **file**        | path on the filesystem to write new file to. |

## Return Value

Returns 0 if successful, -1 on error

## Remarks

If the file already exists, it will be overwritten.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_SavePNG_RW](IMG_SavePNG_RW.md)
* [IMG_SaveJPG](IMG_SaveJPG.md)
* [IMG_SaveJPG_RW](IMG_SaveJPG_RW.md)

----
[CategoryAPI](CategoryAPI.md)
