# SDL_GL_ExtensionSupported

Check if an OpenGL extension is supported for the current context.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GL_ExtensionSupported(const char *extension);
```

## Function Parameters

|              |               |                                     |
| ------------ | ------------- | ----------------------------------- |
| const char * | **extension** | the name of the extension to check. |

## Return Value

(bool) Returns true if the extension is supported, false otherwise.

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

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## Code Examples

```c
    extern void draw_to_the_screen_with_framebuffer_blit(void);
    extern void draw_to_the_screen_with_a_textured_quad(void);

    if (SDL_GL_ExtensionSupported("GL_EXT_framebuffer_blit")) {
        draw_to_the_screen_with_framebuffer_blit();   // faster!
    } else {
        draw_to_the_screen_with_a_textured_quad();  // slower!
    }

```





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

