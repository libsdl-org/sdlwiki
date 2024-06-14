###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SavePNG

Save an SDL_Surface into a PNG image file.

## Header File

Defined in [<SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/SDL2/include/SDL_image.h)

## Syntax

```c
int IMG_SavePNG(SDL_Surface *surface, const char *file);
```

## Function Parameters

|               |             |                                              |
| ------------- | ----------- | -------------------------------------------- |
| SDL_Surface * | **surface** | the SDL surface to save.                     |
| const char *  | **file**    | path on the filesystem to write new file to. |

## Return Value

(int) Returns 0 if successful, -1 on error.

## Remarks

If the file already exists, it will be overwritten.

## Version

This function is available since SDL_image 2.0.0.

## See Also

- [IMG_SavePNG_RW](IMG_SavePNG_RW)
- [IMG_SaveJPG](IMG_SaveJPG)
- [IMG_SaveJPG_RW](IMG_SaveJPG_RW)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

