#include <stdio.h>
#include "SDL.h"
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>
#include <SDL3/SDL_timer.h>

int main(int argc, char* argv[])
{
    // returns zero on success else non-zero
    if (SDL_Init(SDL_INIT_EVERYTHING) != 0)
    {
        printf("error initializing SDL: %s\n", SDL_GetError());
        return 1;
    }
    SDL_Window* win = SDL_CreateWindow("GAME", // creates a window
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        1000, 1000, 0);

    // triggers the program that controls
    // your graphics hardware and sets flags
    Uint render_flags = SDL_RENDERER_ACCELERATED;

    // creates a renderer to render images
    SDL_Renderer* rend = SDL_CreateRenderer(win, -1, render_flags);

    ///
    /// Section 2: SDL image loader
    ///

    ///
    /// Section 4: SDL ttf and rendering text
    ///

    ///
    /// Section 3: Game Loop and Basic Controls
    ///

    // Add a delay in order to see that the window
    // has successfully popped up.
    SDL_Delay(3000);

    ///
    /// Section 5: Freeing resources
    ///

    // Destroy the window. Passing in the pointer
    // that points to the memory allocated by the
    // 'SDL_CreateWindow' function.
    SDL_DestroyWindow(win);

    // Safely uninitialize SDL3 by
    // taking down the subsystems before
    // exiting the program
    SDL_Quit();
}