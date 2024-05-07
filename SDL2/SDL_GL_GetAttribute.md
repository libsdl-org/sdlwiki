###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_GetAttribute

Get the actual value for an attribute from the current context.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GL_GetAttribute(SDL_GLattr attr, int *value);

```

## Function Parameters

|               |                                                                               |
| ------------- | ----------------------------------------------------------------------------- |
| **attr**      | an [SDL_GLattr](SDL_GLattr) enum value specifying the OpenGL attribute to get |
| **value**     | a pointer filled in with the current value of `attr`                          |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GL_ResetAttributes](SDL_GL_ResetAttributes)
- [SDL_GL_SetAttribute](SDL_GL_SetAttribute)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

