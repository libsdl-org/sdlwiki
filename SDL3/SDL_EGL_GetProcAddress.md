###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EGL_GetProcAddress

Get an EGL library function by name.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_FunctionPointer SDL_EGL_GetProcAddress(const char *proc);
```

## Function Parameters

|              |          |                             |
| ------------ | -------- | --------------------------- |
| const char * | **proc** | the name of an EGL function |

## Return Value

([SDL_FunctionPointer](SDL_FunctionPointer)) Returns a pointer to the named
EGL function. The returned pointer should be cast to the appropriate
function signature.

## Remarks

If an EGL library is loaded, this function allows applications to get entry
points for EGL functions. This is useful to provide to an EGL API and
extension loader.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GL_GetCurrentEGLDisplay](SDL_GL_GetCurrentEGLDisplay)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

