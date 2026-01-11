#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

int main(int argc, char *argv[]) {
  // 1. Initialize SDL
  if (!SDL_Init(SDL_INIT_VIDEO)) {
    SDL_Log("Error on initialize SDL: %s", SDL_GetError());
    return 1;
  }

  // 2. Create the Window and Renderer
  // We define a window of 800x600 pixels.
  SDL_Window *window = NULL;
  SDL_Renderer *renderer = NULL;

  // In SDL3, we can create the window and the renderer at the same time for convenience.
  if (!SDL_CreateWindowAndRenderer("Hello World SDL3", 800, 600, 0, &window, &renderer)) {
    SDL_Log("Error creating window/renderer: %s", SDL_GetError());
    SDL_Quit();
    return 1;
  }

  // 3. The Main Loop (Game Loop)
  int running = 1; // Control variable to keep the window open
  SDL_Event event;

  while (running) {
    // Process events (keyboard, mouse, close window)
    while (SDL_PollEvent(&event)) {
      // If the event is "QUIT" (click the X on the window)
      if (event.type == SDL_EVENT_QUIT) {
        running = 0; // Ends the loop
      }
    }

    // 4. Draw on the screen
    // Set the background color (R, G, B, Alpha). Here we use a dark blue.
    SDL_SetRenderDrawColor(renderer, 0, 0, 100, 255);
    // Clear the screen with the color defined above
    SDL_RenderClear(renderer);
    // Update the window with what we drew (present the frame)
    SDL_RenderPresent(renderer);
  }

  // 5. Cleanup and Exit
  // Destroy the created objects to free up memory
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();
  return 0;
}