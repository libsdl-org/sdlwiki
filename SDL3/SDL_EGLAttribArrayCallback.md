# SDL_EGLAttribArrayCallback

EGL platform attribute initialization callback.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef SDL_EGLAttrib *(SDLCALL *SDL_EGLAttribArrayCallback)(void *userdata);
```

## Function Parameters

|              |                                                           |
| ------------ | --------------------------------------------------------- |
| **userdata** | an app-controlled pointer that is passed to the callback. |

## Return Value

Returns a newly-allocated array of attributes, terminated with `EGL_NONE`.

## Remarks

This is called when SDL is attempting to create an EGL context, to let the
app add extra attributes to its eglGetPlatformDisplay() call.

The callback should return a pointer to an EGL attribute array terminated
with `EGL_NONE`. If this function returns NULL, the
[SDL_CreateWindow](SDL_CreateWindow) process will fail gracefully.

The returned pointer should be allocated with [SDL_malloc](SDL_malloc)()
and will be passed to [SDL_free](SDL_free)().

The arrays returned by each callback will be appended to the existing
attribute arrays defined by SDL.

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_EGL_SetAttributeCallbacks](SDL_EGL_SetAttributeCallbacks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryVideo](CategoryVideo)

