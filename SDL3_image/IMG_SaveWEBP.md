###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveWEBP

Save an SDL_Surface into a WEBP image file.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_SaveWEBP(SDL_Surface *surface, const char *file, float quality);
```

## Function Parameters

|               |             |                                                                                                                                                                                                                                             |
| ------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SDL_Surface * | **surface** | the SDL surface to save.                                                                                                                                                                                                                    |
| const char *  | **file**    | path on the filesystem to write the new file to.                                                                                                                                                                                            |
| float         | **quality** | between 0 and 100. For lossy, 0 gives the smallest size and 100 the largest. For lossless, this parameter is the amount of effort put into the compression: 0 is the fastest but gives larger files compared to the slowest, but best, 100. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If the file already exists, it will be overwritten.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_SaveWEBP_IO](IMG_SaveWEBP_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

