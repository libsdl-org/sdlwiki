###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveJPG

Save an SDL_Surface into a JPEG image file.

## Header File

Defined in [<SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/SDL2/include/SDL_image.h)

## Syntax

```c
int IMG_SaveJPG(SDL_Surface *surface, const char *file, int quality);
```

## Function Parameters

|               |             |                                                                                      |
| ------------- | ----------- | ------------------------------------------------------------------------------------ |
| SDL_Surface * | **surface** | the SDL surface to save.                                                             |
| const char *  | **file**    | path on the filesystem to write new file to.                                         |
| int           | **quality** | [0; 33] is Lowest quality, [34; 66] is Middle quality, [67; 100] is Highest quality. |

## Return Value

(int) Returns 0 if successful, -1 on error.

## Remarks

If the file already exists, it will be overwritten.

## Version

This function is available since SDL_image 2.0.2.

## See Also

- [IMG_SaveJPG_RW](IMG_SaveJPG_RW)
- [IMG_SavePNG](IMG_SavePNG)
- [IMG_SavePNG_RW](IMG_SavePNG_RW)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

