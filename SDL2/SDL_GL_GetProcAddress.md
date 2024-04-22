###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_GetProcAddress

Get an OpenGL function by name.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void* SDL_GL_GetProcAddress(const char *proc);

```

## Function Parameters

|              |                                |
| ------------ | ------------------------------ |
| **proc**     | the name of an OpenGL function |

## Return Value

Returns a pointer to the named OpenGL function. The returned pointer should
be cast to the appropriate function signature.

## Remarks

If the GL library is loaded at runtime with
[SDL_GL_LoadLibrary](SDL_GL_LoadLibrary)(), then all GL functions must be
retrieved this way. Usually this is used to retrieve function pointers to
OpenGL extensions.

There are some quirks to looking up OpenGL functions that require some
extra care from the application. If you code carefully, you can handle
these quirks without any platform-specific code, though:

- On Windows, function pointers are specific to the current GL context;
  this means you need to have created a GL context and made it current
  before calling [SDL_GL_GetProcAddress](SDL_GL_GetProcAddress)(). If you
  recreate your context or create a second context, you should assume that
  any existing function pointers aren't valid to use with it. This is
  (currently) a Windows-specific limitation, and in practice lots of
  drivers don't suffer this limitation, but it is still the way the wgl API
  is documented to work and you should expect crashes if you don't respect
  it. Store a copy of the function pointers that comes and goes with
  context lifespan.
- On X11, function pointers returned by this function are valid for any
  context, and can even be looked up before a context is created at all.
  This means that, for at least some common OpenGL implementations, if you
  look up a function that doesn't exist, you'll get a non-NULL result that
  is _NOT_ safe to call. You must always make sure the function is actually
  available for a given GL context before calling it, by checking for the
  existence of the appropriate extension with
  [SDL_GL_ExtensionSupported](SDL_GL_ExtensionSupported)(), or verifying
  that the version of OpenGL you're using offers the function as core
  functionality.
- Some OpenGL drivers, on all platforms, *will* return NULL if a function
  isn't supported, but you can't count on this behavior. Check for
  extensions you use, and if you get a NULL anyway, act as if that
  extension wasn't available. This is probably a bug in the driver, but you
  can code defensively for this scenario anyhow.
- Just because you're on Linux/Unix, don't assume you'll be using X11.
  Next-gen display servers are waiting to replace it, and may or may not
  make the same promises about function pointers.
- OpenGL function pointers must be declared `APIENTRY` as in the example
  code. This will ensure the proper calling convention is followed on
  platforms where this matters (Win32) thereby avoiding stack corruption.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GL_ExtensionSupported](SDL_GL_ExtensionSupported)
* [SDL_GL_LoadLibrary](SDL_GL_LoadLibrary)
* [SDL_GL_UnloadLibrary](SDL_GL_UnloadLibrary)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

