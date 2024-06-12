###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveAVIF

Save an SDL_Surface into a AVIF image file.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
int IMG_SaveAVIF(SDL_Surface *surface, const char *file, int quality);
```

## Function Parameters

|               |             |                                                                   |
| ------------- | ----------- | ----------------------------------------------------------------- |
| SDL_Surface * | **surface** | the SDL surface to save                                           |
| const char *  | **file**    | path on the filesystem to write new file to.                      |
| int           | **quality** | the desired quality, ranging between 0 (lowest) and 100 (highest) |

## Return Value

(int) Returns 0 if successful, -1 on error

## Remarks

If the file already exists, it will be overwritten.

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_SaveAVIF_IO](IMG_SaveAVIF_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

