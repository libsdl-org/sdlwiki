###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetDisplays

Get a list of currently connected displays.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_DisplayID * SDL_GetDisplays(int *count);
```

## Function Parameters

|       |           |                                                                        |
| ----- | --------- | ---------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of displays returned, may be NULL. |

## Return Value

([SDL_DisplayID](SDL_DisplayID) *) Returns a 0 terminated array of display
instance IDs or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information. This should be freed with [SDL_free](SDL_free)() when it
is no longer needed.

## Version

This function is available since SDL 3.1.3.

## Code Examples

```c
// Example program
// Use SDL3 to check how many displays there are

#include <SDL3/SDL_log.h>
#include <SDL3/SDL_main.h>
#include <SDL3/SDL_video.h>

int
main(int argc, char** argv)
{
  if (!SDL_Init(SDL_INIT_VIDEO)) {
    SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
    return 0;
  }

  int num_displays;
  SDL_DisplayID *displays = SDL_GetDisplays(&num_displays);
  SDL_Log("Found %d display(s)", num_displays);

  SDL_free(displays);

  return 0;
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

