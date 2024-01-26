###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadTexture_RW

Load an image from an SDL data source into a GPU texture.

## Syntax

```c
SDL_Texture * IMG_LoadTexture_RW(SDL_Renderer *renderer, SDL_RWops *src, SDL_bool freesrc);

```

## Function Parameters

|                  |                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------- |
| **renderer**     | the SDL_Renderer to use to create the GPU texture.                                 |
| **src**          | an SDL_RWops that data will be read from.                                          |
| **freesrc**      | SDL_TRUE to close/free the SDL_RWops before returning, SDL_FALSE to leave it open. |

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

If `freesrc` is SDL_TRUE, the RWops will be closed before returning,
whether this function succeeds or not. SDL_image reads everything it needs
from the RWops during this call in any case.

There is a separate function to read files from disk without having to deal
with SDL_RWops: `IMG_LoadTexture(renderer, "filename.jpg")` will call this
function and manage those details for you, determining the file type from
the filename's extension.

There is also [IMG_LoadTextureTyped_RW](IMG_LoadTextureTyped_RW)(), which
is equivalent to this function except a file extension (like "BMP", "JPG",
etc) can be specified, in case SDL_image cannot autodetect the file format.

If you would rather decode an image to an SDL_Surface (a buffer of pixels
in CPU memory), call [IMG_Load](IMG_Load)() instead.

When done with the returned texture, the app should dispose of it with a
call to SDL_DestroyTexture().

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_LoadTexture](IMG_LoadTexture)
* [IMG_LoadTextureTyped_RW](IMG_LoadTextureTyped_RW)
* [SDL_DestroyTexture](SDL_DestroyTexture)

----
[CategoryAPI](CategoryAPI)

