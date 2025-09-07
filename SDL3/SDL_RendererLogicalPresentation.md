# SDL_RendererLogicalPresentation

How the logical size is mapped to the output.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
typedef enum SDL_RendererLogicalPresentation
{
    SDL_LOGICAL_PRESENTATION_DISABLED,  /**< There is no logical size in effect */
    SDL_LOGICAL_PRESENTATION_STRETCH,   /**< The rendered content is stretched to the output resolution */
    SDL_LOGICAL_PRESENTATION_LETTERBOX, /**< The rendered content is fit to the largest dimension and the other dimension is letterboxed with the clear color */
    SDL_LOGICAL_PRESENTATION_OVERSCAN,  /**< The rendered content is fit to the smallest dimension and the other dimension extends beyond the output bounds */
    SDL_LOGICAL_PRESENTATION_INTEGER_SCALE   /**< The rendered content is scaled up by integer multiples to fit the output resolution */
} SDL_RendererLogicalPresentation;
```

## Version

This enum is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryRender](CategoryRender)

