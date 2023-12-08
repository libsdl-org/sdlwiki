###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_ExtensionSupported

Check if an OpenGL extension is supported for the current context.

## Syntax

```c
SDL_bool SDL_GL_ExtensionSupported(const char *extension);

```

## Function Parameters

|                   |                                    |
| ----------------- | ---------------------------------- |
| **extension**     | the name of the extension to check |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the extension is supported,
[SDL_FALSE](SDL_FALSE.md) otherwise.

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

This function is available since SDL 3.0.0.

## Code Examples

```c++

    if (SDL_GL_ExtensionSupported("GL_EXT_framebuffer_blit")) {
        draw_to_the_screen_with_framebuffer_blit();   // faster!
    } else {
        draw_to_the_screen_with_a_textured_quad();  // slower!
    }

```

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
