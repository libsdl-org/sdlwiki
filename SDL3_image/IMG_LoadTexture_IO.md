###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadTexture_IO

Load an image from an SDL data source into a GPU texture.

## Header File

Defined in SDL_image.h

## Syntax

```c
SDL_Texture * IMG_LoadTexture_IO(SDL_Renderer *renderer, SDL_IOStream *src, SDL_bool closeio);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **renderer**     | the SDL_Renderer to use to create the GPU texture.                                    |
| **src**          | an SDL_IOStream that data will be read from.                                          |
| **closeio**      | SDL_TRUE to close/free the SDL_IOStream before returning, SDL_FALSE to leave it open. |

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

There is a separate function to read files from disk without having to deal
with SDL_IOStream: `IMG_LoadTexture(renderer, "filename.jpg")` will call
this function and manage those details for you, determining the file type
from the filename's extension.

There is also [IMG_LoadTextureTyped_IO](IMG_LoadTextureTyped_IO)(), which
is equivalent to this function except a file extension (like "BMP", "JPG",
etc) can be specified, in case SDL_image cannot autodetect the file format.

If you would rather decode an image to an SDL_Surface (a buffer of pixels
in CPU memory), call [IMG_Load](IMG_Load)() instead.

When done with the returned texture, the app should dispose of it with a
call to SDL_DestroyTexture().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_LoadTexture](IMG_LoadTexture)
- [IMG_LoadTextureTyped_IO](IMG_LoadTextureTyped_IO)
- [SDL_DestroyTexture](SDL_DestroyTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

