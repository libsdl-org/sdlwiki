###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateWindowWithProperties

Create a window with the specified properties.

## Syntax

```c
SDL_Window* SDL_CreateWindowWithProperties(SDL_PropertiesID props);

```

## Function Parameters

|               |                       |
| ------------- | --------------------- |
| **props**     | the properties to use |

## Return Value

Returns the window that was created or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

These are the supported properties:

- "always-on-top" (boolean) - true if the window should be always on top
- "borderless" (boolean) - true if the window has no window decoration
- "focusable" (boolean) - true if the window should accept keyboard input
  (defaults true)
- "fullscreen" (boolean) - true if the window should start in fullscreen
  mode at desktop resolution
- "height" (number) - the height of the window
- "hidden" (boolean) - true if the window should start hidden
- "high-pixel-density" (boolean) - true if the window uses a high pixel
  density buffer if possible
- "maximized" (boolean) - true if the window should start maximized
- "menu" (boolean) - true if the window is a popup menu
- "metal" (string) - true if the window will be used with Metal rendering
- "minimized" (boolean) - true if the window should start minimized
- "mouse-grabbed" (boolean) - true if the window starts with grabbed mouse
  focus
- "opengl" (boolean) - true if the window will be used with OpenGL
  rendering
- "parent" (pointer) - an [SDL_Window](SDL_Window) that will be the parent
  of this window, required for windows with the "toolip" and "menu"
  properties
- "resizable" (boolean) - true if the window should be resizable
- "title" (string) - the title of the window, in UTF-8 encoding
- "transparent" (string) - true if the window show transparent in the areas
  with alpha of 0
- "tooltip" (boolean) - true if the window is a tooltip
- "utility" (boolean) - true if the window is a utility window, not showing
  in the task bar and window list
- "vulkan" (string) - true if the window will be used with Vulkan rendering
- "width" (number) - the width of the window
- "x" (number) - the x position of the window, or
  [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED), defaults to
  [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED). This is relative to
  the parent for windows with the "parent" property set.
- "y" (number) - the y position of the window, or
  [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED), defaults to
  [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED). This is relative to
  the parent for windows with the "parent" property set.

On macOS:

- "cocoa.window" (pointer) - the (__unsafe_unretained) NSWindow associated
  with the window, if you want to wrap an existing window.
- "cocoa.view" (pointer) - the (__unsafe_unretained) NSView associated with
  the window, defaults to [window contentView]

On Windows:

- "win32.hwnd" (pointer) - the HWND associated with the window, if you want
  to wrap an existing window.
- "win32.pixel_format_hwnd" (pointer) - optional, another window to share
  pixel format with, useful for OpenGL windows

On X11:

- "x11.window" (number) - the X11 Window associated with the window, if you
  want to wrap an existing window.

The [SDL_Window](SDL_Window) is implicitly shown if the "hidden" property
is not set.

Windows with the "tooltip" and "menu" properties are popup windows and have
the behaviors and guidelines outlined in `SDL_CreatePopupWindow()`.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI)

