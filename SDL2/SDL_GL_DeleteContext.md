###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_DeleteContext

Delete an OpenGL context.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_GL_DeleteContext(SDL_GLContext context);

```

## Function Parameters

|                 |                                  |
| --------------- | -------------------------------- |
| **context**     | the OpenGL context to be deleted |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GL_CreateContext](SDL_GL_CreateContext)

----
[CategoryAPI](CategoryAPI)

