###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadTyped_RW

Load an image from an SDL data source into a software surface.

## Syntax

```c
SDL_Surface * IMG_LoadTyped_RW(SDL_RWops *src, SDL_bool freesrc, const char *type);

```

## Function Parameters

|                 |                                                                                    |
| --------------- | ---------------------------------------------------------------------------------- |
| **src**         | an SDL_RWops that data will be read from.                                          |
| **freesrc**     | SDL_TRUE to close/free the SDL_RWops before returning, SDL_FALSE to leave it open. |
| **type**        | a filename extension that represent this data ("BMP", "GIF", "PNG", etc).          |

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

If `freesrc` is SDL_TRUE, the RWops will be closed before returning,
whether this function succeeds or not. SDL_image reads everything it needs
from the RWops during this call in any case.

Even though this function accepts a file type, SDL_image may still try
other decoders that are capable of detecting file type from the contents of
the image data, but may rely on the caller-provided type string for formats
that it cannot autodetect. If `type` is NULL, SDL_image will rely solely on
its ability to guess the format.

There is a separate function to read files from disk without having to deal
with SDL_RWops: `IMG_Load("filename.jpg")` will call this function and
manage those details for you, determining the file type from the filename's
extension.

There is also [IMG_Load_RW](IMG_Load_RW)(), which is equivalent to this
function except that it will rely on SDL_image to determine what type of
data it is loading, much like passing a NULL for type.

If you are using SDL's 2D rendering API, there is an equivalent call to
load images directly into an SDL_Texture for use by the GPU without using a
software surface: call [IMG_LoadTextureTyped_RW](IMG_LoadTextureTyped_RW)()
instead.

When done with the returned surface, the app should dispose of it with a
call to SDL_DestroySurface().

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_Load](IMG_Load)
* [IMG_Load_RW](IMG_Load_RW)
* [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI)

