###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowSurface

Get the SDL surface associated with the window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_Surface* SDL_GetWindowSurface(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the surface associated with the window, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

A new surface will be created with the optimal format for the window, if
necessary. This surface will be freed when the window is destroyed. Do not
free this surface.

This surface will be invalidated if the window is resized. After resizing a
window this function must be called again to return a valid surface.

You may not combine this with 3D or the rendering API on this window.

This function is affected by
[`SDL_HINT_FRAMEBUFFER_ACCELERATION`](SDL_HINT_FRAMEBUFFER_ACCELERATION).

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
#include <SDL3/SDL.h> // include SDL header

int main(int argc, char* argv[])
{
    SDL_Surface *screen; // even with SDL3, we can still bring ancient code back
    SDL_Window *window;
    SDL_Surface *image;

    SDL_Init(SDL_INIT_VIDEO); // init video

    // create the window like normal
    window = SDL_CreateWindow("SDL3 Surface Example", 640, 480, 0);

    // but instead of creating a renderer, we can draw directly to the screen
    screen = SDL_GetWindowSurface(window);

    // let's just show some classic code for reference
    image = SDL_LoadBMP("box.bmp"); // loads image
    SDL_BlitSurface(image, NULL, screen, NULL); // blit it to the screen
    SDL_DestroySurface(image);

    // this works just like SDL_Flip() in SDL 1.2
    SDL_UpdateWindowSurface(window);

    // show image for 2 seconds
    SDL_Delay(2000);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
```

## See Also

- [SDL_DestroyWindowSurface](SDL_DestroyWindowSurface)
- [SDL_WindowHasSurface](SDL_WindowHasSurface)
- [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface)
- [SDL_UpdateWindowSurfaceRects](SDL_UpdateWindowSurfaceRects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

