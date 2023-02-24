###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_ExtensionSupported

Check if an OpenGL extension is supported for the current context.

## Syntax

```c
SDL_bool SDL_GL_ExtensionSupported(const char
                                   *extension);

```

## Function Parameters

|                   |                                    |
| ----------------- | ---------------------------------- |
| **extension**     | the name of the extension to check |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the extension is supported,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This function operates on the current GL context; you must have created a
context and it must be current before calling this function. Do not assume
that all contexts you create will have the same set of extensions
available, or that recreating an existing context will offer the same
extensions again.

While it's probably not a massive overhead, this function is not an O(1)
operation. Check the extensions you care about after creating the GL
context and save that information somewhere instead of calling the function
every time you need to know.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI)

