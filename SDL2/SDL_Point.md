###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Point

The structure that defines a point (integer)

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
typedef struct SDL_Point
{
    int x;
    int y;
} SDL_Point;
```

## Code Examples

```c++
// Example program:
// Using SDL_Point in some places of your code

#include "SDL.h"
#include <stdio.h>

int main(int argc, char *argv[]) {

    SDL_Window *window;

    SDL_Point window_position = {         //    Position of window
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED
    };
    SDL_Point window_size = {640, 480};   //    Size of window

    SDL_Point mouse_position;             //    Mouse position coords

    SDL_Init(SDL_INIT_VIDEO);             //    Initialize SDL2

    // Create an application window with the following settings:
    window = SDL_CreateWindow( 
        "SDL_Point usage",                //    window title
        window_position.x,                //    initial x position
        window_position.y,                //    initial y position
        window_size.x,                    //    width, in pixels
        window_size.y,                    //    height, in pixels
        SDL_WINDOW_OPENGL                 //    flags - see below
    );

    // Check that the window was successfully made
    if (window == NULL) {
        SDL_Log("Could not create window: %s", SDL_GetError());
        return 1;
    }

    SDL_GetMouseState(                    //    Sets mouse_position to...
        &mouse_position.x,                // ...mouse arrow coords on window
        &mouse_position.y
    );

    SDL_Log("Mouse position: x=%i y=%i",  //    Print mouse position
         mouse_position.x, mouse_position.y
    );

    // Close and destroy the window
    SDL_DestroyWindow(window); 

    // Clean up
    SDL_Quit();
    return 0; 
}
```

## See Also

- [SDL_EnclosePoints](SDL_EnclosePoints)
- [SDL_PointInRect](SDL_PointInRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryRect](CategoryRect)


