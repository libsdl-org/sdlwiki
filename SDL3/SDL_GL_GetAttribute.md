# SDL_GL_GetAttribute

Get the actual value for an attribute from the current context.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GL_GetAttribute(SDL_GLAttr attr, int *value);
```

## Function Parameters

|                          |           |                                                       |
| ------------------------ | --------- | ----------------------------------------------------- |
| [SDL_GLAttr](SDL_GLAttr) | **attr**  | the OpenGL attribute to query.                        |
| int *                    | **value** | a pointer filled in with the current value of `attr`. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL's GL attributes are global state, and while you can use related
functions from any thread, you should only use them to prepare a single GL
context at a time.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GL_ResetAttributes](SDL_GL_ResetAttributes)
- [SDL_GL_SetAttribute](SDL_GL_SetAttribute)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

