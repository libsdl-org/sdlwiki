###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateTextureFromSurface

Create a texture from an existing surface.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

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
SDL_Renderer *renderer;

SDL_Surface *surface = SDL_CreateSurface(640, 480, SDL_PIXELFORMAT_RGBA8888);

if (surface == NULL) {
    fprintf(stderr, "CreateRGBSurface failed: %s\n", SDL_GetError());
    exit(1);
}

SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);

if (texture == NULL) {
    fprintf(stderr, "CreateTextureFromSurface failed: %s\n", SDL_GetError());
    exit(1);
}

SDL_DestroySurface(surface);
surface = NULL;
```

## See Also

- [SDL_CreateTexture](SDL_CreateTexture)
- [SDL_CreateTextureWithProperties](SDL_CreateTextureWithProperties)
- [SDL_DestroyTexture](SDL_DestroyTexture)
- [SDL_QueryTexture](SDL_QueryTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

