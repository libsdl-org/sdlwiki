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

The OpenGL context will be created with the current states set through
[SDL_GL_SetAttribute](SDL_GL_SetAttribute)().

The SDL_Window specified must have been created with the SDL_WINDOW_OPENGL
flag, or context creation will fail.

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

## See Also

- [SDL_GL_DestroyContext](SDL_GL_DestroyContext)
- [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

