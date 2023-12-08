###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadTexture

Load an image from a filesystem path into a GPU texture.

## Syntax

```c
SDL_Texture * IMG_LoadTexture(SDL_Renderer *renderer, const char *file);

```

## Function Parameters

|                  |                                                    |
| ---------------- | -------------------------------------------------- |
| **renderer**     | the SDL_Renderer to use to create the GPU texture. |
| **file**         | a path on the filesystem to load an image from.    |

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

There is a separate function to read files from an SDL_RWops, if you need
an i/o abstraction to provide data from anywhere instead of a simple
filesystem read; that function is
[IMG_LoadTexture_RW](IMG_LoadTexture_RW.md)().

If you would rather decode an image to an SDL_Surface (a buffer of pixels
in CPU memory), call [IMG_Load](IMG_Load.md)() instead.

When done with the returned texture, the app should dispose of it with a
call to SDL_DestroyTexture().

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_LoadTextureTyped_RW](IMG_LoadTextureTyped_RW.md)
* [IMG_LoadTexture_RW](IMG_LoadTexture_RW.md)

----
[CategoryAPI](CategoryAPI.md)
