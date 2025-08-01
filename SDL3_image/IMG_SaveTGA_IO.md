###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveTGA_IO

Save an SDL_Surface into TGA image data, via an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_SaveTGA_IO(SDL_Surface *surface, SDL_IOStream *dst);
```

## Function Parameters

|                |             |                                             |
| -------------- | ----------- | ------------------------------------------- |
| SDL_Surface *  | **surface** | the SDL surface to save.                    |
| SDL_IOStream * | **dst**     | the SDL_IOStream to save the image data to. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If you just want to save to a filename, you can use
[IMG_SaveTGA](IMG_SaveTGA)() instead.

## Version

This function is available since SDL_image 3.2.18.

## See Also

- [IMG_SaveTGA](IMG_SaveTGA)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

