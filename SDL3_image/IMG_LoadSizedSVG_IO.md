###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadSizedSVG_IO

Load an SVG image, scaled to a specific size.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
SDL_Surface * IMG_LoadSizedSVG_IO(SDL_IOStream *src, int width, int height);
```

## Function Parameters

|                |            |                                                     |
| -------------- | ---------- | --------------------------------------------------- |
| SDL_IOStream * | **src**    | an SDL_IOStream to load SVG data from.              |
| int            | **width**  | desired width of the generated surface, in pixels.  |
| int            | **height** | desired height of the generated surface, in pixels. |

## Return Value

(SDL_Surface *) Returns a new SDL surface, or NULL on error.

## Remarks

Since SVG files are resolution-independent, you specify the size you would
like the output image to be and it will be generated at those dimensions.

Either width or height may be 0 and the image will be auto-sized to
preserve aspect ratio.

When done with the returned surface, the app should dispose of it with a
call to SDL_DestroySurface().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_LoadSVG_IO](IMG_LoadSVG_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

