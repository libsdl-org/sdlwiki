###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShowWindow

Show a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_ShowWindow(SDL_Window *window);

```

## Function Parameters

|                |                    |
| -------------- | ------------------ |
| **window**     | the window to show |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_Window *window;

SDL_ShowWindow(window);
```

## See Also

* [SDL_HideWindow](SDL_HideWindow)
* [SDL_RaiseWindow](SDL_RaiseWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)


