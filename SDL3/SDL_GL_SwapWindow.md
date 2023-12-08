###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_SwapWindow

Update a window with OpenGL rendering.

## Syntax

```c
int SDL_GL_SwapWindow(SDL_Window *window);

```

## Function Parameters

|                |                      |
| -------------- | -------------------- |
| **window**     | the window to change |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This is used with double-buffered OpenGL contexts, which are the default.

On macOS, make sure you bind 0 to the draw framebuffer before swapping the
window, otherwise nothing will happen. If you aren't using
glBindFramebuffer(), this is the default and you won't have to do anything
extra.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++

SDL_Window* window = SDL_CreateWindow("SDL2/OpenGL Demo", 30, 30, 640, 480, SDL_WINDOW_OPENGL|SDL_WINDOW_RESIZABLE);

/* Create an OpenGL context associated with the window. */
SDL_GLContext glcontext = SDL_GL_CreateContext(window);

/* This makes our buffer swap syncronized with the monitor's vertical refresh */
SDL_GL_SetSwapInterval(1);

/* Clear context */
glClearColor(0,0,0,1);
glClear(GL_COLOR_BUFFER_BIT);

/* <Extra drawing functions here> */

/* Swap our buffer to display the current contents of buffer on screen */
SDL_GL_SwapWindow(window);


```

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
