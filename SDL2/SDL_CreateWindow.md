====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CreateWindow =

Create a window with the specified position, dimensions, and flags.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Window * SDL_CreateWindow(const char *title,
                              int x, int y, int w,
                              int h, Uint32 flags);
</syntaxhighlight>

== Function Parameters ==

{|
|'''title'''
|the title of the window, in UTF-8 encoding
|-
|'''x'''
|the x position of the window, <code>[[SDL_WINDOWPOS_CENTERED]]</code>, or <code>[[SDL_WINDOWPOS_UNDEFINED]]</code>
|-
|'''y'''
|the y position of the window, <code>[[SDL_WINDOWPOS_CENTERED]]</code>, or <code>[[SDL_WINDOWPOS_UNDEFINED]]</code>
|-
|'''w'''
|the width of the window, in screen coordinates
|-
|'''h'''
|the height of the window, in screen coordinates
|-
|'''flags'''
|0, or one or more [[SDL_WindowFlags]] OR'd together
|}

== Return Value ==

Returns the window that was created or NULL on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

<code>flags</code> may be any of the following OR'd together:

* <code>[[SDL_WINDOW_FULLSCREEN]]</code>: fullscreen window
* <code>[[SDL_WINDOW_FULLSCREEN_DESKTOP]]</code>: fullscreen window at desktop resolution
* <code>[[SDL_WINDOW_OPENGL]]</code>: window usable with an OpenGL context
* <code>[[SDL_WINDOW_VULKAN]]</code>: window usable with a Vulkan instance
* <code>[[SDL_WINDOW_METAL]]</code>: window usable with a Metal instance
* <code>[[SDL_WINDOW_HIDDEN]]</code>: window is not visible
* <code>[[SDL_WINDOW_BORDERLESS]]</code>: no window decoration
* <code>[[SDL_WINDOW_RESIZABLE]]</code>: window can be resized
* <code>[[SDL_WINDOW_MINIMIZED]]</code>: window is minimized
* <code>[[SDL_WINDOW_MAXIMIZED]]</code>: window is maximized
* <code>[[SDL_WINDOW_INPUT_GRABBED]]</code>: window has grabbed input focus
* <code>[[SDL_WINDOW_ALLOW_HIGHDPI]]</code>: window should be created in high-DPI mode if supported (>= SDL 2.0.1)

<code>[[SDL_WINDOW_SHOWN]]</code> is ignored by [[SDL_CreateWindow]](). The
[[SDL_Window]] is implicitly shown if [[SDL_WINDOW_HIDDEN]] is not set.
<code>[[SDL_WINDOW_SHOWN]]</code> may be queried later using
[[SDL_GetWindowFlags]]().

On Apple's macOS, you '''must''' set the NSHighResolutionCapable Info.plist
property to YES, otherwise you will not receive a High-DPI OpenGL canvas.

If the window is created with the <code>[[SDL_WINDOW_ALLOW_HIGHDPI]]</code>
flag, its size in pixels may differ from its size in screen coordinates on
platforms with high-DPI support (e.g. iOS and macOS). Use
[[SDL_GetWindowSize]]() to query the client area's size in screen
coordinates, and [[SDL_GL_GetDrawableSize]]() or
[[SDL_GetRendererOutputSize]]() to query the drawable size in pixels. Note
that when this flag is set, the drawable size can vary after the window is
created and should be queried after major window events such as when the
window is resized or moved between displays.

If the window is set fullscreen, the width and height parameters
<code>w</code> and <code>h</code> will not be used. However, invalid size
parameters (e.g. too large) may still fail. Window size is actually limited
to 16384 x 16384 for all platforms at window creation.

If the window is created with any of the [[SDL_WINDOW_OPENGL]] or
[[SDL_WINDOW_VULKAN]] flags, then the corresponding LoadLibrary function
([[SDL_GL_LoadLibrary]] or [[SDL_Vulkan_LoadLibrary]]) is called and the
corresponding UnloadLibrary function is called by [[SDL_DestroyWindow]]().

If [[SDL_WINDOW_VULKAN]] is specified and there isn't a working Vulkan
driver, [[SDL_CreateWindow]]() will fail because
[[SDL_Vulkan_LoadLibrary]]() will fail.

If [[SDL_WINDOW_METAL]] is specified on an OS that does not support Metal,
[[SDL_CreateWindow]]() will fail.

On non-Apple devices, SDL requires you to either not link to the Vulkan
loader or link to a dynamic library version. This limitation may be removed
in a future version of SDL.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateWindowFrom]]
:[[SDL_DestroyWindow]]

----
[[CategoryAPI]]


