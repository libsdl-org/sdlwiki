###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateTexture

Create a texture for a rendering context.

## Syntax

```c
SDL_Texture* SDL_CreateTexture(SDL_Renderer *renderer, Uint32 format, int access, int w, int h);

```

## Function Parameters

|                  |                                                                            |
| ---------------- | -------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                      |
| **format**       | one of the enumerated values in [SDL_PixelFormatEnum](SDL_PixelFormatEnum) |
| **access**       | one of the enumerated values in [SDL_TextureAccess](SDL_TextureAccess)     |
| **w**            | the width of the texture in pixels                                         |
| **h**            | the height of the texture in pixels                                        |

## Return Value

Returns a pointer to the created texture or NULL if no rendering context
was active, the format was unsupported, or the width or height were out of
range; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can set the texture scaling method by setting
[`SDL_HINT_RENDER_SCALE_QUALITY`](SDL_HINT_RENDER_SCALE_QUALITY) before
creating the texture.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include "SDL.h"

/* Moving Rectangle */
int main(int argc, char *argv[])
{
        SDL_Window *window;
        SDL_Renderer *renderer;
        SDL_Texture *texture;
        SDL_Event event;
        SDL_Rect r;

        if (SDL_Init(SDL_INIT_VIDEO) < 0) {
                SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't initialize SDL: %s", SDL_GetError());
                return 3;
        }

        window = SDL_CreateWindow("SDL_CreateTexture",
                        SDL_WINDOWPOS_UNDEFINED,
                        SDL_WINDOWPOS_UNDEFINED,
                        1024, 768,
                        SDL_WINDOW_RESIZABLE);

        r.w = 100;
        r.h = 50;

        renderer = SDL_CreateRenderer(window, NULL, 0);

        texture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_RGBA8888, SDL_TEXTUREACCESS_TARGET, 1024, 768);

        while (1) {
                SDL_PollEvent(&event);
                if(event.type == SDL_EVENT_QUIT)
                        break;
                r.x=rand()%500;
                r.y=rand()%500;

                SDL_SetRenderTarget(renderer, texture);
                SDL_SetRenderDrawColor(renderer, 0x00, 0x00, 0x00, 0x00);
                SDL_RenderClear(renderer);
                SDL_RenderRect(renderer,&r);
                SDL_SetRenderDrawColor(renderer, 0xFF, 0x00, 0x00, 0x00);
                SDL_RenderFillRect(renderer, &r);
                SDL_SetRenderTarget(renderer, NULL);
                SDL_RenderTexture(renderer, texture, NULL, NULL);
                SDL_RenderPresent(renderer);
        }
        SDL_DestroyRenderer(renderer);
        SDL_Quit();
        return 0;
}

```

## Related Functions

* [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface)
* [SDL_CreateTextureWithProperties](SDL_CreateTextureWithProperties)
* [SDL_DestroyTexture](SDL_DestroyTexture)
* [SDL_QueryTexture](SDL_QueryTexture)
* [SDL_UpdateTexture](SDL_UpdateTexture)

----
[CategoryAPI](CategoryAPI), [CategoryRender](CategoryRender)


