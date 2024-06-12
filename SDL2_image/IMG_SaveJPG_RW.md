###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveJPG_RW

Save an SDL_Surface into JPEG image data, via an SDL_RWops.

## Header File

Defined in [<SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/SDL2/include/SDL_image.h)

## Syntax

```c
int IMG_SaveJPG_RW(SDL_Surface *surface, SDL_RWops *dst, int freedst, int quality);
```

## Function Parameters

|               |             |                                          |
| ------------- | ----------- | ---------------------------------------- |
| SDL_Surface * | **surface** | the SDL surface to save                  |
| SDL_RWops *   | **dst**     | the SDL_RWops to save the image data to. |

## Return Value

(int) Returns 0 if successful, -1 on error.

## Remarks

If you just want to save to a filename, you can use
[IMG_SaveJPG](IMG_SaveJPG)() instead.

## Version

This function is available since SDL_image 2.0.2.

## See Also

- [IMG_SaveJPG](IMG_SaveJPG)
- [IMG_SavePNG](IMG_SavePNG)
- [IMG_SavePNG_RW](IMG_SavePNG_RW)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

