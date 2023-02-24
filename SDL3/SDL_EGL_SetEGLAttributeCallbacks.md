###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EGL_SetEGLAttributeCallbacks

Sets the callbacks for defining custom EGLAttrib arrays for EGL initialization.

## Syntax

```c
void SDL_EGL_SetEGLAttributeCallbacks(SDL_EGLAttribArrayCallback platformAttribCallback,
                                      SDL_EGLIntArrayCallback surfaceAttribCallback,
                                      SDL_EGLIntArrayCallback contextAttribCallback);

```

## Function Parameters

|                                |                                                           |
| ------------------------------ | --------------------------------------------------------- |
| **platformAttribCallback**     | Callback for attributes to pass to eglGetPlatformDisplay. |
| **surfaceAttribCallback**      | Callback for attributes to pass to eglCreateSurface.      |
| **contextAttribCallback**      | Callback for attributes to pass to eglCreateContext.      |

## Remarks

Each callback should return a pointer to an EGL attribute array terminated
with EGL_NONE. Callbacks may return NULL pointers to signal an error, which
will cause the [SDL_CreateWindow](SDL_CreateWindow) process to fail
gracefully.

The arrays returned by each callback will be appended to the existing
attribute arrays defined by SDL.

NOTE: These callback pointers will be reset after
[SDL_GL_ResetAttributes](SDL_GL_ResetAttributes).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

