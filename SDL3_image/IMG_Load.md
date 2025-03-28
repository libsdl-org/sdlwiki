###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_Load

Load an image from a filesystem path into a software surface.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
SDL_Surface * IMG_Load(const char *file);
```

## Function Parameters

|              |          |                                                 |
| ------------ | -------- | ----------------------------------------------- |
| const char * | **file** | a path on the filesystem to load an image from. |

## Return Value

(SDL_Surface *) Returns a new SDL surface, or NULL on error.

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

There is a separate function to read files from an SDL_IOStream, if you
need an i/o abstraction to provide data from anywhere instead of a simple
filesystem read; that function is [IMG_Load_IO](IMG_Load_IO)().

If you are using SDL's 2D rendering API, there is an equivalent call to
load images directly into an SDL_Texture for use by the GPU without using a
software surface: call [IMG_LoadTexture](IMG_LoadTexture)() instead.

When done with the returned surface, the app should dispose of it with a
call to
[SDL_DestroySurface](https://wiki.libsdl.org/SDL3/SDL_DestroySurface)
().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_LoadTyped_IO](IMG_LoadTyped_IO)
- [IMG_Load_IO](IMG_Load_IO)
- [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

