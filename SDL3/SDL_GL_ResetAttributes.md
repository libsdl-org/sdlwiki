# SDL_GL_ResetAttributes

Reset all previously set OpenGL context attributes to their default values.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
void SDL_GL_ResetAttributes(void);
```

## Remarks

SDL's GL attributes are global state, and while you can use related
functions from any thread, you should only use them to prepare a single GL
context at a time.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GL_GetAttribute](SDL_GL_GetAttribute)
- [SDL_GL_SetAttribute](SDL_GL_SetAttribute)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

