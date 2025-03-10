# SDL_GL_CreateContext

Create an OpenGL context for an OpenGL window, and make it current.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_GLContext SDL_GL_CreateContext(SDL_Window *window);
```

## Function Parameters

|                            |            |                                           |
| -------------------------- | ---------- | ----------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to associate with the context. |

## Return Value

([SDL_GLContext](SDL_GLContext)) Returns the OpenGL context associated with
`window` or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

Windows users new to OpenGL should note that, for historical reasons, GL
functions added after OpenGL version 1.1 are not available by default.
Those functions must be loaded at run-time, either with an OpenGL
extension-handling library or with
[SDL_GL_GetProcAddress](SDL_GL_GetProcAddress)() and its related functions.

[SDL_GLContext](SDL_GLContext) is opaque to the application.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## Code Examples

```c

// Window mode MUST include SDL_WINDOW_OPENGL for use with OpenGL.
SDL_Window *window = SDL_CreateWindow(
    "SDL3/OpenGL Demo", 640, 480, 
    SDL_WINDOW_OPENGL|SDL_WINDOW_RESIZABLE);
  
// Create an OpenGL context associated with the window.
SDL_GLContext glcontext = SDL_GL_CreateContext(window);

// now you can make GL calls.
glClearColor(0,0,0,1);
glClear(GL_COLOR_BUFFER_BIT);
SDL_GL_SwapWindow(window);

// Once finished with OpenGL functions, the SDL_GLContext can be destroyed.
SDL_GL_DestroyContext(glcontext);  
```

## See Also

- [SDL_GL_DestroyContext](SDL_GL_DestroyContext)
- [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

