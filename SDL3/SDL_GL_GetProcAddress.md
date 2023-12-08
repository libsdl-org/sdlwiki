###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_GetProcAddress

Get an OpenGL function by name.

## Syntax

```c
SDL_FunctionPointer SDL_GL_GetProcAddress(const char *proc);

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
[SDL_GL_LoadLibrary](SDL_GL_LoadLibrary.md)(), then all GL functions must be
retrieved this way. Usually this is used to retrieve function pointers to
OpenGL extensions.

There are some quirks to looking up OpenGL functions that require some
extra care from the application. If you code carefully, you can handle
these quirks without any platform-specific code, though:

- On Windows, function pointers are specific to the current GL context;
  this means you need to have created a GL context and made it current
  before calling [SDL_GL_GetProcAddress](SDL_GL_GetProcAddress.md)(). If you
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
  [SDL_GL_ExtensionSupported](SDL_GL_ExtensionSupported.md)(), or verifying
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

This function is available since SDL 3.0.0.

## Code Examples

```c++
typedef void (APIENTRY * GL_ActiveTextureARB_Func)(unsigned int);
GL_ActiveTextureARB_Func glActiveTextureARB_ptr = 0;

/* Get function pointer */
glActiveTextureARB_ptr=(GL_ActiveTextureARB_Func) SDL_GL_GetProcAddress("glActiveTextureARB");

/* It was your responsibility to make sure this was a valid function to call! */
glActiveTextureARB_ptr(GL_TEXTURE0_ARB);
```

## Related Functions

* [SDL_GL_ExtensionSupported](SDL_GL_ExtensionSupported.md)
* [SDL_GL_LoadLibrary](SDL_GL_LoadLibrary.md)
* [SDL_GL_UnloadLibrary](SDL_GL_UnloadLibrary.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
