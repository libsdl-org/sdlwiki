###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateShapedWindow

Create a window that can be shaped with the specified position, dimensions, and flags.

## Syntax

```c
SDL_Window * SDL_CreateShapedWindow(const char *title,unsigned int x,unsigned int y,unsigned int w,unsigned int h,Uint32 flags);

```

## Function Parameters

|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **title**     | The title of the window, in UTF-8 encoding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **x**         | The x position of the window, ::[SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED.md), or ::[SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED.md).                                                                                                                                                                                                                                                                                                                                                                                                      |
| **y**         | The y position of the window, ::[SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED.md), or ::[SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED.md).                                                                                                                                                                                                                                                                                                                                                                                                      |
| **w**         | The width of the window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **h**         | The height of the window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **flags**     | The flags for the window, a mask of [SDL_WINDOW_BORDERLESS](SDL_WINDOW_BORDERLESS.md) with any of the following: ::[SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL.md), ::[SDL_WINDOW_INPUT_GRABBED](SDL_WINDOW_INPUT_GRABBED.md), ::[SDL_WINDOW_HIDDEN](SDL_WINDOW_HIDDEN.md), ::[SDL_WINDOW_RESIZABLE](SDL_WINDOW_RESIZABLE.md), ::[SDL_WINDOW_MAXIMIZED](SDL_WINDOW_MAXIMIZED.md), ::[SDL_WINDOW_MINIMIZED](SDL_WINDOW_MINIMIZED.md), ::[SDL_WINDOW_BORDERLESS](SDL_WINDOW_BORDERLESS.md) is always set, and ::[SDL_WINDOW_FULLSCREEN](SDL_WINDOW_FULLSCREEN.md) is always unset. |

## Return Value

Return the window created, or NULL if window creation failed.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_DestroyWindow](SDL_DestroyWindow.md)

----
[CategoryAPI](CategoryAPI.md)
