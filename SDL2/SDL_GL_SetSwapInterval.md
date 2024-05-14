###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_SetSwapInterval

Set the swap interval for the current OpenGL context.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GL_SetSwapInterval(int interval);

```

## Function Parameters

|                  |                                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| **interval**     | 0 for immediate updates, 1 for updates synchronized with the vertical retrace, -1 for adaptive vsync |

## Return Value

Returns 0 on success or -1 if setting the swap interval is not supported;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Some systems allow specifying -1 for the interval, to enable adaptive
vsync. Adaptive vsync works the same as vsync, but if you've already missed
the vertical retrace for a given frame, it swaps buffers immediately, which
might be less jarring for the user during occasional framerate drops. If an
application requests adaptive vsync and the system does not support it,
this function will fail and return -1. In such a case, you should probably
retry the call with 1 for the interval.

Adaptive vsync is implemented for some glX drivers with
GLX_EXT_swap_control_tear, and for some Windows drivers with
WGL_EXT_swap_control_tear.

Read more on the Khronos wiki:
https://www.khronos.org/opengl/wiki/Swap_Interval#Adaptive_Vsync

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GL_GetSwapInterval](SDL_GL_GetSwapInterval)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

