###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateShapedWindow

Create a window that can be shaped with the specified dimensions and flags.

## Syntax

```c
SDL_Window* SDL_CreateShapedWindow(const char *title, int w, int h, Uint32 flags);

```

## Function Parameters

|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **title**     | The title of the window, in UTF-8 encoding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **w**         | The width of the window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **h**         | The height of the window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **flags**     | The flags for the window, a mask of [SDL_WINDOW_BORDERLESS](SDL_WINDOW_BORDERLESS) with any of the following: ::[SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL), ::[SDL_WINDOW_MOUSE_GRABBED](SDL_WINDOW_MOUSE_GRABBED), ::[SDL_WINDOW_HIDDEN](SDL_WINDOW_HIDDEN), ::[SDL_WINDOW_RESIZABLE](SDL_WINDOW_RESIZABLE), ::[SDL_WINDOW_MAXIMIZED](SDL_WINDOW_MAXIMIZED), ::[SDL_WINDOW_MINIMIZED](SDL_WINDOW_MINIMIZED), ::[SDL_WINDOW_BORDERLESS](SDL_WINDOW_BORDERLESS) is always set, and ::[SDL_WINDOW_FULLSCREEN](SDL_WINDOW_FULLSCREEN) is always unset. |

## Return Value

Returns the window created, or NULL if window creation failed.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI)

