###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_EGL_SetAttributeCallbacks

Sets the callbacks for defining custom EGLAttrib arrays for EGL initialization.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
void SDL_EGL_SetAttributeCallbacks(SDL_EGLAttribArrayCallback platformAttribCallback,
                                   SDL_EGLIntArrayCallback surfaceAttribCallback,
                                   SDL_EGLIntArrayCallback contextAttribCallback, void *userdata);
```

## Function Parameters

|                                                          |                            |                                                                        |
| -------------------------------------------------------- | -------------------------- | ---------------------------------------------------------------------- |
| [SDL_EGLAttribArrayCallback](SDL_EGLAttribArrayCallback) | **platformAttribCallback** | callback for attributes to pass to eglGetPlatformDisplay. May be NULL. |
| [SDL_EGLIntArrayCallback](SDL_EGLIntArrayCallback)       | **surfaceAttribCallback**  | callback for attributes to pass to eglCreateSurface. May be NULL.      |
| [SDL_EGLIntArrayCallback](SDL_EGLIntArrayCallback)       | **contextAttribCallback**  | callback for attributes to pass to eglCreateContext. May be NULL.      |
| void *                                                   | **userdata**               | a pointer that is passed to the callbacks.                             |

## Remarks

Callbacks that aren't needed can be set to NULL.

NOTE: These callback pointers will be reset after
[SDL_GL_ResetAttributes](SDL_GL_ResetAttributes).

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

