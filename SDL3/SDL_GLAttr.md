###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GLAttr

An enumeration of OpenGL configuration attributes.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef enum SDL_GLAttr
{
    SDL_GL_RED_SIZE,                    /**< the minimum number of bits for the red channel of the color buffer; defaults to 3. */
    SDL_GL_GREEN_SIZE,                  /**< the minimum number of bits for the green channel of the color buffer; defaults to 3. */
    SDL_GL_BLUE_SIZE,                   /**< the minimum number of bits for the blue channel of the color buffer; defaults to 2. */
    SDL_GL_ALPHA_SIZE,                  /**< the minimum number of bits for the alpha channel of the color buffer; defaults to 0. */
    SDL_GL_BUFFER_SIZE,                 /**< the minimum number of bits for frame buffer size; defaults to 0. */
    SDL_GL_DOUBLEBUFFER,                /**< whether the output is single or double buffered; defaults to double buffering on. */
    SDL_GL_DEPTH_SIZE,                  /**< the minimum number of bits in the depth buffer; defaults to 16. */
    SDL_GL_STENCIL_SIZE,                /**< the minimum number of bits in the stencil buffer; defaults to 0. */
    SDL_GL_ACCUM_RED_SIZE,              /**< the minimum number of bits for the red channel of the accumulation buffer; defaults to 0. */
    SDL_GL_ACCUM_GREEN_SIZE,            /**< the minimum number of bits for the green channel of the accumulation buffer; defaults to 0. */
    SDL_GL_ACCUM_BLUE_SIZE,             /**< the minimum number of bits for the blue channel of the accumulation buffer; defaults to 0. */
    SDL_GL_ACCUM_ALPHA_SIZE,            /**< the minimum number of bits for the alpha channel of the accumulation buffer; defaults to 0. */
    SDL_GL_STEREO,                      /**< whether the output is stereo 3D; defaults to off. */
    SDL_GL_MULTISAMPLEBUFFERS,          /**< the number of buffers used for multisample anti-aliasing; defaults to 0. */
    SDL_GL_MULTISAMPLESAMPLES,          /**< the number of samples used around the current pixel used for multisample anti-aliasing. */
    SDL_GL_ACCELERATED_VISUAL,          /**< set to 1 to require hardware acceleration, set to 0 to force software rendering; defaults to allow either. */
    SDL_GL_RETAINED_BACKING,            /**< not used (deprecated). */
    SDL_GL_CONTEXT_MAJOR_VERSION,       /**< OpenGL context major version. */
    SDL_GL_CONTEXT_MINOR_VERSION,       /**< OpenGL context minor version. */
    SDL_GL_CONTEXT_FLAGS,               /**< some combination of 0 or more of elements of the SDL_GLContextFlag enumeration; defaults to 0. */
    SDL_GL_CONTEXT_PROFILE_MASK,        /**< type of GL context (Core, Compatibility, ES). See SDL_GLProfile; default value depends on platform. */
    SDL_GL_SHARE_WITH_CURRENT_CONTEXT,  /**< OpenGL context sharing; defaults to 0. */
    SDL_GL_FRAMEBUFFER_SRGB_CAPABLE,    /**< requests sRGB capable visual; defaults to 0. */
    SDL_GL_CONTEXT_RELEASE_BEHAVIOR,    /**< sets context the release behavior. See SDL_GLContextReleaseFlag; defaults to FLUSH. */
    SDL_GL_CONTEXT_RESET_NOTIFICATION,  /**< set context reset notification. See SDL_GLContextResetNotification; defaults to NO_NOTIFICATION. */
    SDL_GL_CONTEXT_NO_ERROR,
    SDL_GL_FLOATBUFFERS,
    SDL_GL_EGL_PLATFORM
} SDL_GLAttr;
```

## Remarks

While you can set most OpenGL attributes normally, the attributes listed
above must be known before SDL creates the window that will be used with
the OpenGL context. These attributes are set and read with
[SDL_GL_SetAttribute](SDL_GL_SetAttribute)() and
[SDL_GL_GetAttribute](SDL_GL_GetAttribute)().

In some cases, these attributes are minimum requests; the GL does not
promise to give you exactly what you asked for. It's possible to ask for a
16-bit depth buffer and get a 24-bit one instead, for example, or to ask
for no stencil buffer and still have one available. Context creation should
fail if the GL can't provide your requested attributes at a minimum, but
you should check to see exactly what you got.

## Version

This enum is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryVideo](CategoryVideo)

