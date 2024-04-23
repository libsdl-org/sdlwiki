###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_SwapWindow

Update a window with OpenGL rendering.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_GL_SwapWindow(SDL_Window * window);

```

## Function Parameters

|                |                      |
| -------------- | -------------------- |
| **window**     | the window to change |

## Remarks

This is used with double-buffered OpenGL contexts, which are the default.

On macOS, make sure you bind 0 to the draw framebuffer before swapping the
window, otherwise nothing will happen. If you aren't using
glBindFramebuffer(), this is the default and you won't have to do anything
extra.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

