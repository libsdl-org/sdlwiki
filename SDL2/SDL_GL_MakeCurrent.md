###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_MakeCurrent

Set up an OpenGL context for rendering into an OpenGL window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_GL_MakeCurrent(SDL_Window * window,
                       SDL_GLContext context);

```

## Function Parameters

|                 |                                                 |
| --------------- | ----------------------------------------------- |
| **window**      | the window to associate with the context        |
| **context**     | the OpenGL context to associate with the window |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The context must have been created with a compatible window.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GL_CreateContext](SDL_GL_CreateContext)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

