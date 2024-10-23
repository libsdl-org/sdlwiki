###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GL_LoadLibrary

Dynamically load an OpenGL library.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GL_LoadLibrary(const char *path);
```

## Function Parameters

|              |          |                                                                                         |
| ------------ | -------- | --------------------------------------------------------------------------------------- |
| const char * | **path** | the platform dependent OpenGL library name, or NULL to open the default OpenGL library. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This should be done after initializing the video driver, but before
creating any OpenGL windows. If no OpenGL library is loaded, the default
library will be loaded upon creation of the first OpenGL window.

If you do this, you need to retrieve all of the GL functions used in your
program from the dynamic library using
[SDL_GL_GetProcAddress](SDL_GL_GetProcAddress)().

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GL_GetProcAddress](SDL_GL_GetProcAddress)
- [SDL_GL_UnloadLibrary](SDL_GL_UnloadLibrary)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

