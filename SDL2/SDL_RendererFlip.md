###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RendererFlip

Flip constants for [SDL_RenderCopyEx](SDL_RenderCopyEx)

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
typedef enum SDL_RendererFlip
{
    SDL_FLIP_NONE = 0x00000000,     /**< Do not flip */
    SDL_FLIP_HORIZONTAL = 0x00000001,    /**< flip horizontally */
    SDL_FLIP_VERTICAL = 0x00000002     /**< flip vertically */
} SDL_RendererFlip;
```

## Code Examples

```c
extern SDL_Renderer *renderer;
extern SDL_Texture *texture;
extern SDL_Rect srcrect;
extern SDL_Rect dstrect;
extern int angle;
extern SDL_Point center;

/* casts may be necessary for some compiler settings or languages (e.g. C++) */
SDL_RendererFlip flip = SDL_FLIP_HORIZONTAL | SDL_FLIP_VERTICAL;

SDL_RenderCopyEx(renderer, texture, &srcrect, &dstrect, angle, &center, flip);
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryRender](CategoryRender)

