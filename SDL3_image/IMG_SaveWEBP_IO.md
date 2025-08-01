###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveWEBP_IO

Save an SDL_Surface into WEBP image data, via an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_SaveWEBP_IO(SDL_Surface *surface, SDL_IOStream *dst, bool closeio, float quality);
```

## Function Parameters

|                |             |                                                                                                                                                                                                                                             |
| -------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SDL_Surface *  | **surface** | the SDL surface to save.                                                                                                                                                                                                                    |
| SDL_IOStream * | **dst**     | the SDL_IOStream to save the image data to.                                                                                                                                                                                                 |
| bool           | **closeio** | true to close/free the SDL_IOStream before returning, false to leave it open.                                                                                                                                                               |
| float          | **quality** | between 0 and 100. For lossy, 0 gives the smallest size and 100 the largest. For lossless, this parameter is the amount of effort put into the compression: 0 is the fastest but gives larger files compared to the slowest, but best, 100. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If you just want to save to a filename, you can use
[IMG_SaveWEBP](IMG_SaveWEBP)() instead.

If `closeio` is true, `dst` will be closed before returning, whether this
function succeeds or not.

## Version

This function is available since SDL_image 3.2.18.

## See Also

- [IMG_SaveWEBP](IMG_SaveWEBP)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

