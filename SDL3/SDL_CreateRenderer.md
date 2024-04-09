###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateRenderer

Create a 2D rendering context for a window.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_Renderer * SDL_CreateRenderer(SDL_Window *window, const char *name, Uint32 flags);

```

## Function Parameters

|                |                                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| **window**     | the window where rendering is displayed                                                                            |
| **name**       | the name of the rendering driver to initialize, or NULL to initialize the first one supporting the requested flags |
| **flags**      | 0, or one or more [SDL_RendererFlags](SDL_RendererFlags) OR'd together                                             |

## Return Value

Returns a valid rendering context or NULL if there was an error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If you want a specific renderer, you can specify its name here. A list of
available renderers can be obtained by calling
[SDL_GetRenderDriver](SDL_GetRenderDriver) multiple times, with indices
from 0 to [SDL_GetNumRenderDrivers](SDL_GetNumRenderDrivers)()-1. If you
don't need a specific renderer, specify NULL and SDL will attempt to choose
the best option for you, based on what is available on the user's system.

By default the rendering size matches the window size in pixels, but you
can call
[SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)() to
change the content size and scaling options.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

int main(int argc, char *argv[])
{
    SDL_Window *win = NULL;
    SDL_Renderer *renderer = NULL;
    SDL_Texture *bitmapTex = NULL;
    SDL_Surface *bitmapSurface = NULL;
    int width = 320, height = 240;
    SDL_bool loopShouldStop = SDL_FALSE;

    SDL_Init(SDL_INIT_VIDEO);

    win = SDL_CreateWindow("Hello World", width, height, 0);

    renderer = SDL_CreateRenderer(win, NULL, 0);

    bitmapSurface = SDL_LoadBMP("img/hello.bmp");
    bitmapTex = SDL_CreateTextureFromSurface(renderer, bitmapSurface);
    SDL_DestroySurface(bitmapSurface);

    while (!loopShouldStop)
    {
        SDL_Event event;
        while (SDL_PollEvent(&event))
        {
            switch (event.type)
            {
                case SDL_EVENT_QUIT:
                    loopShouldStop = SDL_TRUE;
                    break;
            }
        }

        SDL_RenderClear(renderer);
        SDL_RenderTexture(renderer, bitmapTex, NULL, NULL);
        SDL_RenderPresent(renderer);
    }

    SDL_DestroyTexture(bitmapTex);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(win);

    SDL_Quit();

    return 0;
}
```

## See Also

* [SDL_CreateRendererWithProperties](SDL_CreateRendererWithProperties)
* [SDL_CreateSoftwareRenderer](SDL_CreateSoftwareRenderer)
* [SDL_DestroyRenderer](SDL_DestroyRenderer)
* [SDL_GetNumRenderDrivers](SDL_GetNumRenderDrivers)
* [SDL_GetRenderDriver](SDL_GetRenderDriver)
* [SDL_GetRendererInfo](SDL_GetRendererInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)


