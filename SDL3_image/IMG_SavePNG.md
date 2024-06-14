###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SavePNG

Save an SDL_Surface into a PNG image file.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

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

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_SavePNG_IO](IMG_SavePNG_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

