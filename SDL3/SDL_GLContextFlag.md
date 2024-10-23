###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GLContextFlag

Possible flags to be set for the [SDL_GL_CONTEXT_FLAGS](SDL_GL_CONTEXT_FLAGS) attribute.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef Uint32 SDL_GLContextFlag;

#define SDL_GL_CONTEXT_DEBUG_FLAG              0x0001
#define SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG 0x0002
#define SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG      0x0004
#define SDL_GL_CONTEXT_RESET_ISOLATION_FLAG    0x0008
```

## Version

This datatype is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryVideo](CategoryVideo)

