###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateColorCursor

Create a color cursor.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_Cursor* SDL_CreateColorCursor(SDL_Surface *surface,
                                  int hot_x,
                                  int hot_y);

```

## Function Parameters

|                 |                                                                       |
| --------------- | --------------------------------------------------------------------- |
| **surface**     | an [SDL_Surface](SDL_Surface) structure representing the cursor image |
| **hot_x**       | the x position of the cursor hot spot                                 |
| **hot_y**       | the y position of the cursor hot spot                                 |

## Return Value

Returns the new cursor on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include <SDL3/SDL.h>

int
main(int argc, char *argv[])
{
    SDL_Window *window = NULL;
    SDL_Renderer *renderer = NULL;
    SDL_Surface *surface = NULL;
    SDL_Cursor *cursor = NULL;
    SDL_bool error = SDL_TRUE;

    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        goto exit;
    }
    if (SDL_CreateWindowAndRenderer("Hello SDL", 640, 480, 0, &window, &renderer) < 0) {
        goto exit;
    }
    surface = SDL_LoadBMP((1 < argc) ? argv[1] : "cursor.bmp");
    if (!surface) {
        goto exit;
    }
    cursor = SDL_CreateColorCursor(surface, 0, 0);
    if (!cursor) {
        goto exit;
    }

    SDL_SetCursor(cursor);
    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
    while (SDL_TRUE) {
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            switch (event.type) {
            case SDL_EVENT_MOUSE_BUTTON_UP:
            case SDL_EVENT_QUIT:
                error = SDL_FALSE;
                goto exit;
            }
        }
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
    }

exit:
    if (error) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "%s", SDL_GetError());
    }
    if (cursor) {
        SDL_DestroyCursor(cursor);
    }
    if (surface) {
        SDL_DestroySurface(surface);
    }
    if (renderer) {
        SDL_DestroyRenderer(renderer);
    }
    if (window) {
        SDL_DestroyWindow(window);
    }
    SDL_Quit();
    return error;
}
```

## See Also

- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_CreateSystemCursor](SDL_CreateSystemCursor)
- [SDL_DestroyCursor](SDL_DestroyCursor)
- [SDL_SetCursor](SDL_SetCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

