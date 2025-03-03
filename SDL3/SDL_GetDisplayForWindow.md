# SDL_GetDisplayForWindow

Get the display associated with a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_DisplayID SDL_GetDisplayForWindow(SDL_Window *window);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query. |

## Return Value

([SDL_DisplayID](SDL_DisplayID)) Returns the instance ID of the display
containing the center of the window on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## Code Examples

```c
// Example program
// Use SDL3 to log which display a window was created on

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

  SDL_Window* window = SDL_CreateWindow("My Window", 640, 480, 0);
  if(window == NULL) {
    SDL_Log("Unable to create window: %s", SDL_GetError());
    return 0;
  }

  SDL_DisplayID display_id = SDL_GetDisplayForWindow(window);
  SDL_Log("Window created on display '%s'", SDL_GetDisplayName(display_id));

  SDL_DestroyWindow(window);

  return 0;
}
```

## See Also

- [SDL_GetDisplayBounds](SDL_GetDisplayBounds)
- [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

