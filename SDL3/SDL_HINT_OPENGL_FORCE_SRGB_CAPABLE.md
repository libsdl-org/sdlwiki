# SDL_HINT_OPENGL_FORCE_SRGB_CAPABLE

A variable controlling whether to force an sRGB-capable OpenGL context.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_OPENGL_FORCE_SRGB_CAPABLE "SDL_OPENGL_FORCE_SRGB_CAPABLE"
```

## Remarks

At OpenGL context creation time, some platforms can request an sRGB-capable
context. However, sometimes any form of the request can cause surprising
results on some drivers, platforms, and hardware. Usually the surprise is
in the form of rendering that is either a little darker or a little
brighter than intended.

This hint allows the user to override the app's sRGB requests and either
force a specific value, or avoid requesting anything at all, depending on
what makes things work correctly for their system.

This is meant as a fail-safe; apps should probably not explicitly set this,
and most users should not, either.

Note that some platforms cannot make this request at all, and on all
platforms this request can be denied by the operating system.

The variable can be set to the following values:

- "0": Force a request for an OpenGL context that is _not_ sRGB-capable.
- "1": Force a request for an OpenGL context that _is_ sRGB-capable.
- "skip": Don't make any request for an sRGB-capable context (don't specify
  the attribute at all during context creation time).
- any other string is undefined behavior.

If unset, or set to an empty string, SDL will make a request using the
value the app specified with the
[SDL_GL_FRAMEBUFFER_SRGB_CAPABLE](SDL_GL_FRAMEBUFFER_SRGB_CAPABLE)
attribute.

This hint should be set before an OpenGL context is created.

## Version

This hint is available since SDL 3.4.2.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

