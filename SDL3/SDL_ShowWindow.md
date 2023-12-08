###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShowWindow

Show a window.

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
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_ShowWindow(window);
```

## Related Functions

* [SDL_HideWindow](SDL_HideWindow.md)
* [SDL_RaiseWindow](SDL_RaiseWindow.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
