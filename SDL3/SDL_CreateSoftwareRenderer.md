###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateSoftwareRenderer

Create a 2D software rendering context for a surface.

## Syntax

```c
SDL_Renderer* SDL_CreateSoftwareRenderer(SDL_Surface *surface);

```

## Function Parameters

|                 |                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure representing the surface where rendering is done |

## Return Value

Returns a valid rendering context or NULL if there was an error; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Two other API which can be used to create [SDL_Renderer](SDL_Renderer.md):
[SDL_CreateRenderer](SDL_CreateRenderer.md)() and
[SDL_CreateWindowAndRenderer](SDL_CreateWindowAndRenderer.md)(). These can
_also_ create a software renderer, but they are intended to be used with an
[SDL_Window](SDL_Window.md) as the final destination and not an
[SDL_Surface](SDL_Surface.md).

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include "SDL.h"

SDL_Window *window;
SDL_Renderer *renderer;
int done;

void
DrawChessBoard(SDL_Renderer * renderer)
{
    int row = 0,column = 0,x = 0;
    SDL_Rect rect, darea;

    /* Get the Size of drawing surface */
    SDL_GetRenderViewport(renderer, &darea);

    for ( ; row < 8; row++) {
        column = row%2;
        x = column;
        for ( ; column < 4+(row%2); column++) {
            SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0xFF);

            rect.w = darea.w/8;
            rect.h = darea.h/8;
            rect.x = x * rect.w;
            rect.y = row * rect.h;
            x = x + 2;
            SDL_RenderFillRect(renderer, &rect);
        }
    }
}

void
loop()
{
    SDL_Event e;
    while (SDL_PollEvent(&e)) {
        if (e.type == SDL_EVENT_QUIT) {
            done = 1;
            return;
        }

        if ((e.type == SDL_EVENT_KEY_DOWN) && (e.key.keysym.sym == SDLK_ESCAPE)) {
            done = 1;
            return;
        }
    }

    DrawChessBoard(renderer);

    /* Got everything on rendering surface,
       now Update the drawing image on window screen */
    SDL_UpdateWindowSurface(window);
}

int
main(int argc, char *argv[])
{
    SDL_Surface *surface;

    /* Enable standard application logging */
    SDL_LogSetPriority(SDL_LOG_CATEGORY_APPLICATION, SDL_LOG_PRIORITY_INFO);

    /* Initialize SDL */
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "SDL_Init fail : %s\n", SDL_GetError());
        return 1;
    }

    /* Create window and renderer for given surface */
    window = SDL_CreateWindow("Chess Board", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 0);
    if (!window) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Window creation fail : %s\n",SDL_GetError());
        return 1;
    }
    surface = SDL_GetWindowSurface(window);
    renderer = SDL_CreateSoftwareRenderer(surface);
    if (!renderer) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Render creation for surface fail : %s\n",SDL_GetError());
        return 1;
    }

    /* Clear the rendering surface with the specified color */
    SDL_SetRenderDrawColor(renderer, 0xFF, 0xFF, 0xFF, 0xFF);
    SDL_RenderClear(renderer);

    /* Draw the Image on rendering surface */
    done = 0;

    while (!done) {
        loop();
    }

    SDL_Quit();
    return 0;
}
```

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer.md)
* [SDL_CreateWindowRenderer](SDL_CreateWindowRenderer.md)
* [SDL_DestroyRenderer](SDL_DestroyRenderer.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
