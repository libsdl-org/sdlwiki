# SDL_ALPHA_OPAQUE

This macro represents the maximum opacity value (255), indicating that the surface is fully opaque.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_ALPHA_OPAQUE 255
```

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
SDL_SetRenderDrawColor(renderer, 80, 80, 80, SDL_ALPHA_OPAQUE);
SDL_RenderClear(renderer);
SDL_RenderPresent(renderer);
```

## See Also

- [SDL_SetRenderDrawColor](https://wiki.libsdl.org/SDL3/SDL_SetRenderDrawColor)