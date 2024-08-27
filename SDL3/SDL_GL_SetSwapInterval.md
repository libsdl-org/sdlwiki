###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_SetSwapInterval

Set the swap interval for the current OpenGL context.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_GL_SetSwapInterval(int interval);
```

## Function Parameters

|     |              |                                                                                                       |
| --- | ------------ | ----------------------------------------------------------------------------------------------------- |
| int | **interval** | 0 for immediate updates, 1 for updates synchronized with the vertical retrace, -1 for adaptive vsync. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

Some systems allow specifying -1 for the interval, to enable adaptive
vsync. Adaptive vsync works the same as vsync, but if you've already missed
the vertical retrace for a given frame, it swaps buffers immediately, which
might be less jarring for the user during occasional framerate drops. If an
application requests adaptive vsync and the system does not support it,
this function will fail and return [SDL_FALSE](SDL_FALSE). In such a case,
you should probably retry the call with 1 for the interval.

Adaptive vsync is implemented for some glX drivers with
GLX_EXT_swap_control_tear, and for some Windows drivers with
WGL_EXT_swap_control_tear.

Read more on the Khronos wiki:
https://www.khronos.org/opengl/wiki/Swap_Interval#Adaptive_Vsync

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GL_GetSwapInterval](SDL_GL_GetSwapInterval)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

