###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateTextureFromSurface

Create a texture from an existing surface.

## Syntax

```c
SDL_Texture* SDL_CreateTextureFromSurface(SDL_Renderer *renderer, SDL_Surface *surface);

```

## Function Parameters

|                  |                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                   |
| **surface**      | the [SDL_Surface](SDL_Surface) structure containing pixel data used to fill the texture |

## Return Value

Returns the created texture or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The surface is not modified or freed by this function.

The [SDL_TextureAccess](SDL_TextureAccess) hint for the created texture is
[`SDL_TEXTUREACCESS_STATIC`](SDL_TEXTUREACCESS_STATIC).

The pixel format of the created texture may be different from the pixel
format of the surface. Use [SDL_QueryTexture](SDL_QueryTexture)() to query
the pixel format of the texture.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
Uint32 rmask, gmask, bmask, amask;

/* SDL interprets each pixel as a 32-bit number, so our masks must depend
   on the endianness (byte order) of the machine */
#if SDL_BYTEORDER == SDL_BIG_ENDIAN
    rmask = 0xff000000;
    gmask = 0x00ff0000;
    bmask = 0x0000ff00;
    amask = 0x000000ff;
#else
    rmask = 0x000000ff;
    gmask = 0x0000ff00;
    bmask = 0x00ff0000;
    amask = 0xff000000;
#endif

SDL_Surface *surface = SDL_CreateRGBSurface(0, 640, 480, 32, rmask, gmask, bmask, amask);

if (surface == NULL) {
    fprintf(stderr, "CreateRGBSurface failed: %s\n", SDL_GetError());
    exit(1);
}


SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);

if (texture == NULL) {
    fprintf(stderr, "CreateTextureFromSurface failed: %s\n", SDL_GetError());
    exit(1);
}

SDL_FreeSurface(surface);
surface = NULL;

```

## Related Functions

* [SDL_CreateTexture](SDL_CreateTexture)
* [SDL_DestroyTexture](SDL_DestroyTexture)
* [SDL_QueryTexture](SDL_QueryTexture)

----
[CategoryAPI](CategoryAPI), [CategoryRender](CategoryRender)


