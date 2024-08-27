###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_GetAttribute

Get the actual value for an attribute from the current context.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_GL_GetAttribute(SDL_GLattr attr, int *value);
```

## Function Parameters

|                          |           |                                                                                |
| ------------------------ | --------- | ------------------------------------------------------------------------------ |
| [SDL_GLattr](SDL_GLattr) | **attr**  | an [SDL_GLattr](SDL_GLattr) enum value specifying the OpenGL attribute to get. |
| int *                    | **value** | a pointer filled in with the current value of `attr`.                          |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GL_ResetAttributes](SDL_GL_ResetAttributes)
- [SDL_GL_SetAttribute](SDL_GL_SetAttribute)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

