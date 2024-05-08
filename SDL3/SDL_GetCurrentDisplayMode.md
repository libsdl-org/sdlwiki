###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentDisplayMode

Get information about the current display mode.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const SDL_DisplayMode* SDL_GetCurrentDisplayMode(SDL_DisplayID displayID);

```

## Function Parameters

|                   |                                         |
| ----------------- | --------------------------------------- |
| **displayID**     | the instance ID of the display to query |

## Return Value

Returns a pointer to the desktop display mode or NULL on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

There's a difference between this function and
[SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode)() when SDL runs
fullscreen and has changed the resolution. In that case this function will
return the current display mode, and not the previous native display mode.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++

// Using SDL2's SDL_GetCurrentDisplayMode()

#include <SDL3/SDL.h>

int main(int argc, char* argv[])
{
  int i;

  // Declare display mode structure to be filled in.
  SDL_DisplayMode current;

  SDL_Init(SDL_INIT_VIDEO);
  
  int count_displays;
  SDL_DisplayID *displays = SDL_GetDisplays(&count_displays);

  // Get current display mode of all displays.
  for(i = 0; i < count_displays; i++){

    const SDL_DisplayMode *display_mode = SDL_GetCurrentDisplayMode(displays[i]);

    if (display_mode== NULL) {
      // In case of error...
      SDL_Log("Could not get display mode for video display #%d: %s", i, SDL_GetError());
    } else {
      // On success, print the current display mode.
      SDL_Log("Display #%d: current display mode is %dx%dpx @ %dhz.", i, display_mode->w, display_mode->h, display_mode->refresh_rate);
    }
  }

  // Clean up and exit the program.
  SDL_free(displays);
  SDL_Quit();
  return 0;
}

```

## See Also

- [SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode)
- [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

