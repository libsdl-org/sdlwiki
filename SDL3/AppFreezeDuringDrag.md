# Why does my app freeze while the window is being resized or dragged/moved?

On some operating systems (notably Windows, but others as well), your call into [`SDL_PollEvent`](SDL_PollEvent), [`SDL_WaitEvent`](SDL_WaitEvent), [`SDL_WaitEventTimeout`](SDL_WaitEventTimeout), or [`SDL_PumpEvents`](SDL_PumpEvents) may block during resizing or dragging. This means these functions will not return and yield control to your code, until the OS is done with this operation, so new frames of video won't render, and other tasks, like game logic and multiplayer network upkeep, will not have a chance to run. The delay will last as long as the user is dragging or resizing the window in this case, which might be several seconds or more!

The operating systems _do_ provide ways for a user application to still do work during these operations, but they do so through callbacks: a function the user provides and the OS will call at appropriate times.

SDL provides two ways to get called during these blocking operations.
  - [The callbacks from `SDL_main.h`](README-main-functions#main-callbacks-in-sdl3)
    - Using this, [`SDL_AppEvent`](SDL_AppEvent) and [`SDL_AppIterate`](SDL_AppIterate) should be called for you, even when being resized or moved.
  - [SDL_AddEventWatch](SDL_AddEventWatch)
    - Using this, you'll need to watch for the `SDL_EVENT_WINDOW_EXPOSED` event. This event tells you that you should redraw your window from within the callback so it doesn't stretch or look overly unnatural.

For further context, even when blocked the OS gives your application time slices during these operations, but they do so through callbacks themselves, not by returning back to user code. So the only solution is for SDL or similar to give you a callback as well.

This doesn't guarantee perfectly smooth resizing but greatly improves the situation.

Here's a program that demonstrates using the main callbacks, still allowing user code to run during Window resize and move operations:

```c
#include <SDL3/SDL.h>

#define SDL_MAIN_USE_CALLBACKS
#include <SDL3/SDL_main.h>

SDL_Window* g_window;
SDL_Renderer* g_renderer;
SDL_FRect g_rect = {
    100.f, 100.f, 100.f, 100.f
};

SDL_AppResult SDL_AppInit(void** appstate, int argc, char** argv)
{
    SDL_CreateWindowAndRenderer("Test", 300, 300, SDL_WINDOW_RESIZABLE, &g_window, &g_renderer);
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppIterate(void* appstate)
{
    SDL_SetRenderDrawColor(g_renderer, 0, 0, 0, 255);
    SDL_RenderClear(g_renderer);

    SDL_FRect rect = g_rect;
    rect.x += 50 * SDL_sinf(SDL_GetTicksNS() / 1000000000.f);


    SDL_SetRenderDrawColor(g_renderer, 255, 255, 255, 255);
    SDL_RenderFillRect(g_renderer, &rect);


    SDL_RenderPresent(g_renderer);
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppEvent(void* appstate, SDL_Event* event)
{
    if (event->common.type == SDL_EVENT_QUIT) {
        return SDL_APP_SUCCESS;
    }
    return SDL_APP_CONTINUE;
}

void SDL_AppQuit(void* appstate, SDL_AppResult result)
{ 
}
```
