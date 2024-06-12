###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_ReadXPMFromArray

Load an XPM image from a memory array.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
SDL_Surface * IMG_ReadXPMFromArray(char **xpm);
```

## Function Parameters

|         |         |                                                            |
| ------- | ------- | ---------------------------------------------------------- |
| char ** | **xpm** | a null-terminated array of strings that comprise XPM data. |

## Return Value

(SDL_Surface *) Returns a new SDL surface, or NULL on error.

## Remarks

The returned surface will be an 8bpp indexed surface, if possible,
otherwise it will be 32bpp. If you always want 32-bit data, use
[IMG_ReadXPMFromArrayToRGB888](IMG_ReadXPMFromArrayToRGB888)() instead.

When done with the returned surface, the app should dispose of it with a
call to SDL_DestroySurface().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_ReadXPMFromArrayToRGB888](IMG_ReadXPMFromArrayToRGB888)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

