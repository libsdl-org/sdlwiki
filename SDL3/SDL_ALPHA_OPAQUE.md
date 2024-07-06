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
#include <SDL3/SDL.h>

int main(int argc, char* argv[])
{
        SDL_Window* window;
        SDL_Renderer* renderer;

        /* Initialize SDL. */
        if (SDL_Init(SDL_INIT_VIDEO) < 0)
                return 1;

        /* Create the window where we will draw. */
        window = SDL_CreateWindow("SDL_RenderClear",
                        512, 512,
                        0);

        /* We must call SDL_CreateRenderer in order for draw calls to affect this window. */
        renderer = SDL_CreateRenderer(window, NULL);

        /* Select the color for drawing. It is set to red here. */
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, SDL_ALPHA_OPAQUE);

        /* Clear the entire screen to our selected color. */
        SDL_RenderClear(renderer);

        /* Up until now everything was drawn behind the scenes.
           This will show the new, red contents of the window. */
        SDL_RenderPresent(renderer);

        /* Give us time to see the window. */
        SDL_Delay(5000);

        /* Always be sure to clean up */
        SDL_Quit();
        return 0;
}
```

## See Also

- [SDL_SetRenderDrawColor](https://wiki.libsdl.org/SDL3/SDL_SetRenderDrawColor)