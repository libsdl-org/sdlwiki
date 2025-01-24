# SDL_GetDisplayName

Get the name of a display in UTF-8 encoding.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const char * SDL_GetDisplayName(SDL_DisplayID displayID);
```

## Function Parameters

|                                |               |                                          |
| ------------------------------ | ------------- | ---------------------------------------- |
| [SDL_DisplayID](SDL_DisplayID) | **displayID** | the instance ID of the display to query. |

## Return Value

(const char *) Returns the name of a display or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## Code Examples

```c
// Example program
// Use SDL3 to log the name of every display found

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

  for(int i = 0; i < num_displays; i++) {
    SDL_Log("Found display named '%s'", SDL_GetDisplayName(displays[i]));
  }

  SDL_free(displays);

  return 0;
}
```

## See Also

- [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

