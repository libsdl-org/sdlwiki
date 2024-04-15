###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_OPENGL_ES_DRIVER

A variable controlling what driver to use for OpenGL ES contexts.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_OPENGL_ES_DRIVER   "SDL_OPENGL_ES_DRIVER"
```

## Remarks

On some platforms, currently Windows and X11, OpenGL drivers may support
creating contexts with an OpenGL ES profile. By default SDL uses these
profiles, when available, otherwise it attempts to load an OpenGL ES
library, e.g. that provided by the ANGLE project. This variable controls
whether SDL follows this default behaviour or will always load an OpenGL ES
library.

Circumstances where this is useful include - Testing an app with a
particular OpenGL ES implementation, e.g ANGLE, or emulator, e.g. those
from ARM, Imagination or Qualcomm. - Resolving OpenGL ES function addresses
at link time by linking with the OpenGL ES library instead of querying them
at run time with [SDL_GL_GetProcAddress](SDL_GL_GetProcAddress)().

Caution: for an application to work with the default behaviour across
different OpenGL drivers it must query the OpenGL ES function addresses at
run time using [SDL_GL_GetProcAddress](SDL_GL_GetProcAddress)().

This variable is ignored on most platforms because OpenGL ES is native or
not supported.

The variable can be set to the following values:

- "0": Use ES profile of OpenGL, if available. (default)
- "1": Load OpenGL ES library using the default library names.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

