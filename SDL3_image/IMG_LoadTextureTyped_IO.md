###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadTextureTyped_IO

Load an image from an SDL data source into a GPU texture.

## Header File

Defined in SDL_image.h

## Syntax

```c
SDL_Texture * IMG_LoadTextureTyped_IO(SDL_Renderer *renderer, SDL_IOStream *src, SDL_bool closeio, const char *type);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **renderer**     | the SDL_Renderer to use to create the GPU texture.                                    |
| **src**          | an SDL_IOStream that data will be read from.                                          |
| **closeio**      | SDL_TRUE to close/free the SDL_IOStream before returning, SDL_FALSE to leave it open. |
| **type**         | a filename extension that represent this data ("BMP", "GIF", "PNG", etc).             |

## Return Value

Returns a new texture, or NULL on error.

## Remarks

An SDL_Texture represents an image in GPU memory, usable by SDL's 2D Render
API. This can be significantly more efficient than using a CPU-bound
SDL_Surface if you don't need to manipulate the image directly after
loading it.

If the loaded image has transparency or a colorkey, a texture with an alpha
channel will be created. Otherwise, SDL_image will attempt to create an
SDL_Texture in the most format that most reasonably represents the image
data (but in many cases, this will just end up being 32-bit RGB or 32-bit
RGBA).

If `closeio` is SDL_TRUE, `src` will be closed before returning, whether
this function succeeds or not. SDL_image reads everything it needs from
`src` during this call in any case.

Even though this function accepts a file type, SDL_image may still try
other decoders that are capable of detecting file type from the contents of
the image data, but may rely on the caller-provided type string for formats
that it cannot autodetect. If `type` is NULL, SDL_image will rely solely on
its ability to guess the format.

There is a separate function to read files from disk without having to deal
with SDL_IOStream: `IMG_LoadTexture("filename.jpg")` will call this
function and manage those details for you, determining the file type from
the filename's extension.

There is also [IMG_LoadTexture_IO](IMG_LoadTexture_IO)(), which is
equivalent to this function except that it will rely on SDL_image to
determine what type of data it is loading, much like passing a NULL for
type.

If you would rather decode an image to an SDL_Surface (a buffer of pixels
in CPU memory), call [IMG_LoadTyped_IO](IMG_LoadTyped_IO)() instead.

When done with the returned texture, the app should dispose of it with a
call to SDL_DestroyTexture().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_LoadTexture](IMG_LoadTexture)
- [IMG_LoadTexture_IO](IMG_LoadTexture_IO)
- [SDL_DestroyTexture](SDL_DestroyTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

