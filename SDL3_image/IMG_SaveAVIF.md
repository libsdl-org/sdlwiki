###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveAVIF

Save an SDL_Surface into a AVIF image file.

## Header File

Defined in SDL_image.h

## Syntax

```c
int IMG_SaveAVIF(SDL_Surface *surface, const char *file, int quality);

```

## Function Parameters

|                 |                                                                   |
| --------------- | ----------------------------------------------------------------- |
| **surface**     | the SDL surface to save                                           |
| **file**        | path on the filesystem to write new file to.                      |
| **quality**     | the desired quality, ranging between 0 (lowest) and 100 (highest) |

## Return Value

Returns 0 if successful, -1 on error

## Remarks

If the file already exists, it will be overwritten.

## Version

This function is available since SDL_image 3.0.0.

## See Also

* [IMG_SaveAVIF_IO](IMG_SaveAVIF_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

