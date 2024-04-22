###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowTitle

Set the title of a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_SetWindowTitle(SDL_Window *window, const char *title);

```

## Function Parameters

|                |                                          |
| -------------- | ---------------------------------------- |
| **window**     | the window to change                     |
| **title**      | the desired window title in UTF-8 format |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This string is expected to be in UTF-8 encoding.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
// dynamically setting a window title

#include <SDL3/SDL.h>

int main(int argc, char* argv[]){

  SDL_Window *window;
  SDL_Event e;

  const char *titles[] = { // just for fun, let's make the title animate like a marquee and annoy users
    "t", "thi", "this w", "this win", "this windo", "this window's", "this window's ti", "this window's title",
    "chis window's title is", "chih window's title is ", "chih wandnw's title is ", "c  h wandnw'g title is ",
    "c  h  a  nw'g titln is ", "c  h  a  n  g  i  n ig ", "c  h  a  n  g  i  n  g!", "",
    "c  h  a  n  g  i  n  g!", "", "c  h  a  n  g  i  n  g!", "c  h  a  n  g  i  n  g!"
  };

  SDL_Init(SDL_INIT_VIDEO); // Init SDL2

  // Create a window.
  window = SDL_CreateWindow(
    "This will surely be overwritten", 320, 240, SDL_WINDOW_RESIZABLE
  );

  // Enter the main loop. Press any key or hit the x to exit.
  for( ; e.type!=SDL_EVENT_QUIT&&e.type!=SDL_EVENT_KEY_DOWN; SDL_PollEvent(&e)){
    static int i = 0, t = 0;

    if(!(++t%9)){ // every 9th frame...
      SDL_SetWindowTitle(window, titles[i]);            // loop through the
      if(++i >= sizeof(titles)/sizeof(titles[0])) i = 0; // array of titles
    }

    SDL_Delay(10);

  }

  SDL_DestroyWindow(window);
  SDL_Quit();
  return 0;

}
```

## See Also

* [SDL_GetWindowTitle](SDL_GetWindowTitle)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)


