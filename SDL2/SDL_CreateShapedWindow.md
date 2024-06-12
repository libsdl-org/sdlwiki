###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateShapedWindow

Create a window that can be shaped with the specified position, dimensions, and flags.

## Header File

Defined in [SDL_shape.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_shape.h)

## Syntax

```c
SDL_Window * SDL_CreateShapedWindow(const char *title,unsigned int x,unsigned int y,unsigned int w,unsigned int h,Uint32 flags);
```

## Function Parameters

|              |           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| const char * | **title** | The title of the window, in UTF-8 encoding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| unsigned int | **x**     | The x position of the window, [SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED), or [SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED).                                                                                                                                                                                                                                                                                                                                                                                          |
| unsigned int | **y**     | The y position of the window, [SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED), or [SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED).                                                                                                                                                                                                                                                                                                                                                                                          |
| unsigned int | **w**     | The width of the window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| unsigned int | **h**     | The height of the window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Uint32       | **flags** | The flags for the window, a mask of [SDL_WINDOW_BORDERLESS](SDL_WINDOW_BORDERLESS) with any of the following: [SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL), [SDL_WINDOW_INPUT_GRABBED](SDL_WINDOW_INPUT_GRABBED), [SDL_WINDOW_HIDDEN](SDL_WINDOW_HIDDEN), [SDL_WINDOW_RESIZABLE](SDL_WINDOW_RESIZABLE), [SDL_WINDOW_MAXIMIZED](SDL_WINDOW_MAXIMIZED), [SDL_WINDOW_MINIMIZED](SDL_WINDOW_MINIMIZED), [SDL_WINDOW_BORDERLESS](SDL_WINDOW_BORDERLESS) is always set, and [SDL_WINDOW_FULLSCREEN](SDL_WINDOW_FULLSCREEN) is always unset. |

## Return Value

([SDL_Window](SDL_Window) *) Return the window created, or NULL if window
creation failed.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryShape](CategoryShape)

