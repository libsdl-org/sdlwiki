###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MaximizeWindow

Make a window as large as possible.

## Syntax

```c
int SDL_MaximizeWindow(SDL_Window *window);

```

## Function Parameters

|                |                        |
| -------------- | ---------------------- |
| **window**     | the window to maximize |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_MinimizeWindow](SDL_MinimizeWindow)
* [SDL_RestoreWindow](SDL_RestoreWindow)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


