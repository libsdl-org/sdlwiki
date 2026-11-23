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

The [SDL_Window](SDL_Window) specified must have been created with the
[SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL) flag, or context creation will fail.

Windows users new to OpenGL should note that, for historical reasons, GL
functions added after OpenGL version 1.1 are not available by default.
Those functions must be loaded at run-time, either with an OpenGL
extension-handling library or with
[SDL_GL_GetProcAddress](SDL_GL_GetProcAddress)() and its related functions.

[SDL_GLContext](SDL_GLContext) is opaque to the application.

Generally it _should_ be safe to create a context from a background thread,
to be used on that thread, but in case there are platforms that have
trouble with that, the absolute best practice would be:

- Create the context on the main thread.
- Make the current context NULL on the main thread (or set it back to a
  different context).
- Make the new context current from the thread that will be using the new
  context.

This function is, for now, marked as safe to call from any thread; please
send feedback if this turns out to not be true on a given platform.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GL_DestroyContext](SDL_GL_DestroyContext)
- [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

