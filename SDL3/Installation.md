#include <SDL2/SDL.h>
#include <cmath>
#include <iostream>
#include <vector>

const int screenWidth = 640;
const int screenHeight = 480;
const int mapWidth = 8;
const int mapHeight = 8;
const int tileSize = 64;
const float FOV = 3.14159 / 3.0; // 60 degrees

int map[] = {
    1,1,1,1,1,1,1,1,
    1,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,1,
    1,0,0,1,0,0,0,1,
    1,0,0,1,0,0,0,1,
    1,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,1,
    1,1,1,1,1,1,1,1,
};

float px = 100, py = 100; // Player position
float angle = 0.0f;       // Player angle
float moveSpeed = 2.0f;
float rotSpeed = 0.05f;

void drawRay(SDL_Renderer* renderer, float x, float y, float rayAngle) {
    float rayX = cos(rayAngle);
    float rayY = sin(rayAngle);

    for (int d = 0; d < 500; ++d) {
        int testX = (int)(px + rayX * d) / tileSize;
        int testY = (int)(py + rayY * d) / tileSize;

        if (testX >= 0 && testX < mapWidth && testY >= 0 && testY < mapHeight) {
            if (map[testY * mapWidth + testX] == 1) {
                float dist = d * cos(rayAngle - angle);
                int lineHeight = (tileSize * screenHeight) / (dist + 0.01);
                int drawStart = screenHeight / 2 - lineHeight / 2;
                int drawEnd = drawStart + lineHeight;

                SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
                SDL_RenderDrawLine(renderer, x, drawStart, x, drawEnd);
                break;
            }
        }
    }
}

int main() {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window* window = SDL_CreateWindow("Mini FPS", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, screenWidth, screenHeight, 0);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    bool running = true;
    SDL_Event event;

    while (running) {
        // Handle input
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT)
                running = false;
        }

        const Uint8* keys = SDL_GetKeyboardState(NULL);
        if (keys[SDL_SCANCODE_W]) {
            px += cos(angle) * moveSpeed;
            py += sin(angle) * moveSpeed;
        }
        if (keys[SDL_SCANCODE_S]) {
            px -= cos(angle) * moveSpeed;
            py -= sin(angle) * moveSpeed;
        }
        if (keys[SDL_SCANCODE_A]) angle -= rotSpeed;
        if (keys[SDL_SCANCODE_D]) angle += rotSpeed;

        // Draw scene
        SDL_SetRenderDrawColor(renderer, 30, 30, 30, 255);
        SDL_RenderClear(renderer);

        for (int x = 0; x < screenWidth; ++x) {
            float rayAngle = angle - FOV / 2 + FOV * x / screenWidth;
            drawRay(renderer, x, 0, rayAngle);
        }

        SDL_RenderPresent(renderer);
        SDL_Delay(16); // ~60 FPS
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}