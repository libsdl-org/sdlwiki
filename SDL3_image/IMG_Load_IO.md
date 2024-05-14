###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_Load_IO

Load an image from an SDL data source into a software surface.

## Header File

Defined in SDL_image.h

## Syntax

```c
SDL_Surface * IMG_Load_IO(SDL_IOStream *src, SDL_bool closeio);

```

## Function Parameters

|                 |                                                                                       |
| --------------- | ------------------------------------------------------------------------------------- |
| **src**         | an SDL_IOStream that data will be read from.                                          |
| **closeio**     | SDL_TRUE to close/free the SDL_IOStream before returning, SDL_FALSE to leave it open. |

## Return Value

Returns a new SDL surface, or NULL on error.

## Remarks

An SDL_Surface is a buffer of pixels in memory accessible by the CPU. Use
this if you plan to hand the data to something else or manipulate it
further in code.

There are no guarantees about what format the new SDL_Surface data will be;
in many cases, SDL_image will attempt to supply a surface that exactly
matches the provided image, but in others it might have to convert (either
because the image is in a format that SDL doesn't directly support or
because it's compressed data that could reasonably uncompress to various
formats and SDL_image had to pick one). You can inspect an SDL_Surface for
its specifics, and use SDL_ConvertSurface to then migrate to any supported
format.

If the image format supports a transparent pixel, SDL will set the colorkey
for the surface. You can enable RLE acceleration on the surface afterwards
by calling: SDL_SetSurfaceColorKey(image, SDL_RLEACCEL,
image->format->colorkey);

If `closeio` is SDL_TRUE, `src` will be closed before returning, whether
this function succeeds or not. SDL_image reads everything it needs from
`src` during this call in any case.

There is a separate function to read files from disk without having to deal
with SDL_IOStream: `IMG_Load("filename.jpg")` will call this function and
manage those details for you, determining the file type from the filename's
extension.

There is also [IMG_LoadTyped_IO](IMG_LoadTyped_IO)(), which is equivalent
to this function except a file extension (like "BMP", "JPG", etc) can be
specified, in case SDL_image cannot autodetect the file format.

If you are using SDL's 2D rendering API, there is an equivalent call to
load images directly into an SDL_Texture for use by the GPU without using a
software surface: call [IMG_LoadTexture_IO](IMG_LoadTexture_IO)() instead.

When done with the returned surface, the app should dispose of it with a
call to SDL_DestroySurface().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_Load](IMG_Load)
- [IMG_LoadTyped_IO](IMG_LoadTyped_IO)
- [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

