# SDL_GLProfile

Possible values to be set for the [SDL_GL_CONTEXT_PROFILE_MASK](SDL_GL_CONTEXT_PROFILE_MASK) attribute.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef Uint32 SDL_GLProfile;

#define SDL_GL_CONTEXT_PROFILE_CORE           0x0001  /**< OpenGL Core Profile context */
#define SDL_GL_CONTEXT_PROFILE_COMPATIBILITY  0x0002  /**< OpenGL Compatibility Profile context */
#define SDL_GL_CONTEXT_PROFILE_ES             0x0004  /**< GLX_CONTEXT_ES2_PROFILE_BIT_EXT */
```

## Version

This datatype is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryVideo](CategoryVideo)

