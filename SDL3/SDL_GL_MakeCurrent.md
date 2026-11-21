# SDL_GL_MakeCurrent

Set the currently-active OpenGL context.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GL_MakeCurrent(SDL_Window *window, SDL_GLContext context);
```

## Function Parameters

|                                |             |                                                  |
| ------------------------------ | ----------- | ------------------------------------------------ |
| [SDL_Window](SDL_Window) *     | **window**  | the window to associate with the context.        |
| [SDL_GLContext](SDL_GLContext) | **context** | the OpenGL context to associate with the window. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function makes a GL context "current," in all the ways that term
implies in OpenGL.

This is a per-thread state that specifies what context future calls into
OpenGL will operate on. Beyond context creation work, you must have a
current context for the thread before attempting to use OpenGL in any way.

The context must have been created with a compatible window.

## Thread Safety

It is safe to call this function from any thread (as long as a unique GL
context was created for that thread).

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GL_CreateContext](SDL_GL_CreateContext)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

