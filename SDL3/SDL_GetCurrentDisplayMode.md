###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentDisplayMode

Get information about the current display mode.

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
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

There's a difference between this function and
[SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode.md)() when SDL runs
fullscreen and has changed the resolution. In that case this function will
return the current display mode, and not the previous native display mode.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++

// Using SDL2's SDL_GetCurrentDisplayMode()

#include "SDL.h"

int main(int argc, char* argv[])
{
  int i;

  // Declare display mode structure to be filled in.
  SDL_DisplayMode current;

  SDL_Init(SDL_INIT_VIDEO);

  // Get current display mode of all displays.
  for(i = 0; i < SDL_GetNumVideoDisplays(); ++i){

    int should_be_zero = SDL_GetCurrentDisplayMode(i, &current);

    if(should_be_zero != 0)
      // In case of error...
      SDL_Log("Could not get display mode for video display #%d: %s", i, SDL_GetError());

    else
      // On success, print the current display mode.
      SDL_Log("Display #%d: current display mode is %dx%dpx @ %dhz.", i, current.w, current.h, current.refresh_rate);

  }

  // Clean up and exit the program.
  SDL_Quit();
  return 0;

}

```

## Related Functions

* [SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode.md)
* [SDL_GetDisplays](SDL_GetDisplays.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
