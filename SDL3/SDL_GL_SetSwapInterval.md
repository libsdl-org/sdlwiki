# SDL_GL_SetSwapInterval

Set the swap interval for the current OpenGL context.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GL_SetSwapInterval(int interval);
```

## Function Parameters

|     |              |                                                                                                       |
| --- | ------------ | ----------------------------------------------------------------------------------------------------- |
| int | **interval** | 0 for immediate updates, 1 for updates synchronized with the vertical retrace, -1 for adaptive vsync. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Some systems allow specifying -1 for the interval, to enable adaptive
vsync. Adaptive vsync works the same as vsync, but if you've already missed
the vertical retrace for a given frame, it swaps buffers immediately, which
might be less jarring for the user during occasional framerate drops. If an
application requests adaptive vsync and the system does not support it,
this function will fail and return false. In such a case, you should
probably retry the call with 1 for the interval.

Adaptive vsync is implemented for some glX drivers with
GLX_EXT_swap_control_tear, and for some Windows drivers with
WGL_EXT_swap_control_tear.

Read more on the Khronos wiki:
https://www.khronos.org/opengl/wiki/Swap_Interval#Adaptive_Vsync

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GL_GetSwapInterval](SDL_GL_GetSwapInterval)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

