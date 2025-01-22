#include <SDL3/SDL.h>
#include <SDL3/SDL_image.h>
#include <stdio.h>

int main() 
{
    if (SDL_Init(SDL_INIT_VIDEO) < 0) 
{
        printf("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }

    SDL_Window* window = SDL_CreateWindow("Rock Paper Scissors Game", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, SDL_WINDOW_SHOWN);
    if (!window)
 {
        printf("Window could not be created! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer)
 {
        printf("Renderer could not be created! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }

    SDL_Event e;
    int quit = 0;

    // Game loop
    while (!quit) 
{
        while (SDL_PollEvent(&e) != 0) 
{
            if (e.type == SDL_QUIT)
 {
                quit = 1;
            }
        }

        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}