###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_ReadXPMFromArrayToRGB888

Load an XPM image from a memory array.

## Header File

Defined in SDL_image.h

## Syntax

```c
SDL_Surface * IMG_ReadXPMFromArrayToRGB888(char **xpm);

```

## Function Parameters

|             |                                                            |
| ----------- | ---------------------------------------------------------- |
| **xpm**     | a null-terminated array of strings that comprise XPM data. |

## Return Value

Returns a new SDL surface, or NULL on error.

## Remarks

The returned surface will always be a 32-bit RGB surface. If you want 8-bit
indexed colors (and the XPM data allows it), use
[IMG_ReadXPMFromArray](IMG_ReadXPMFromArray)() instead.

When done with the returned surface, the app should dispose of it with a
call to SDL_DestroySurface().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_ReadXPMFromArray](IMG_ReadXPMFromArray)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

