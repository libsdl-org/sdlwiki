#include <SDL2/SDL.h>
#include <math.h>
#include <stdbool.h>

#define SEGMENTS 20
#define LENGTH 20

float x[SEGMENTS], y[SEGMENTS];

void drawSegment(SDL_Renderer* renderer, int i, float tx, float ty) {
    float dx = tx - x[i];
    float dy = ty - y[i];
    float angle = atan2f(dy, dx);

    x[i] = tx - cosf(angle) * LENGTH;
    y[i] = ty - sinf(angle) * LENGTH;

    SDL_RenderDrawLine(renderer, (int)x[i], (int)y[i], (int)tx, (int)ty);
}

int main() {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window* window = SDL_CreateWindow("Reptile Cursor", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 600, 0);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    int mouseX = 400, mouseY = 300;
    for (int i = 0; i < SEGMENTS; i++) {
        x[i] = mouseX;
        y[i] = mouseY;
    }

    bool running = true;
    SDL_Event event;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT)
                running = false;
        }

        SDL_GetMouseState(&mouseX, &mouseY);

        SDL_SetRenderDrawColor(renderer, 15, 23, 42, 255); // Background
        SDL_RenderClear(renderer);

        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255); // Line color
        drawSegment(renderer, 0, mouseX, mouseY);
        for (int i = 1; i < SEGMENTS; i++) {
            drawSegment(renderer, i, x[i - 1], y[i - 1]);
        }

        SDL_RenderPresent(renderer);
        SDL_Delay(16);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
