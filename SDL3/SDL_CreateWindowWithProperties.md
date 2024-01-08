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

- [`SDL_PROPERTY_WINDOW_CREATE_ALWAYS_ON_TOP_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_ALWAYS_ON_TOP_BOOLEAN)
  ("always-on-top"): true if the window should be always on top
- [`SDL_PROPERTY_WINDOW_CREATE_BORDERLESS_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_BORDERLESS_BOOLEAN)
  ("borderless"): true if the window has no window decoration
- [`SDL_PROPERTY_WINDOW_CREATE_FOCUSABLE_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_FOCUSABLE_BOOLEAN)
  ("focusable"): true if the window should accept keyboard input (defaults
  true)
- [`SDL_PROPERTY_WINDOW_CREATE_FULLSCREEN_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_FULLSCREEN_BOOLEAN)
  ("fullscreen"): true if the window should start in fullscreen mode at
  desktop resolution
- [`SDL_PROPERTY_WINDOW_CREATE_HEIGHT_NUMBER`](SDL_PROPERTY_WINDOW_CREATE_HEIGHT_NUMBER)
  ("height"): the height of the window
- [`SDL_PROPERTY_WINDOW_CREATE_HIDDEN_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_HIDDEN_BOOLEAN)
  ("hidden"): true if the window should start hidden
- [`SDL_PROPERTY_WINDOW_CREATE_HIGH_PIXEL_DENSITY_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_HIGH_PIXEL_DENSITY_BOOLEAN)
  ("high-pixel-density"): true if the window uses a high pixel density
  buffer if possible
- [`SDL_PROPERTY_WINDOW_CREATE_MAXIMIZED_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_MAXIMIZED_BOOLEAN)
  ("maximized"): true if the window should start maximized
- [`SDL_PROPERTY_WINDOW_CREATE_MENU_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_MENU_BOOLEAN)
  ("menu"): true if the window is a popup menu
- [`SDL_PROPERTY_WINDOW_CREATE_METAL_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_METAL_BOOLEAN)
  ("metal"): true if the window will be used with Metal rendering
- [`SDL_PROPERTY_WINDOW_CREATE_MINIMIZED_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_MINIMIZED_BOOLEAN)
  ("minimized"): true if the window should start minimized
- [`SDL_PROPERTY_WINDOW_CREATE_MOUSE_GRABBED_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_MOUSE_GRABBED_BOOLEAN)
  ("mouse-grabbed"): true if the window starts with grabbed mouse focus
- [`SDL_PROPERTY_WINDOW_CREATE_OPENGL_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_OPENGL_BOOLEAN)
  ("opengl"): true if the window will be used with OpenGL rendering
- [`SDL_PROPERTY_WINDOW_CREATE_PARENT_POINTER`](SDL_PROPERTY_WINDOW_CREATE_PARENT_POINTER)
  ("parent"): an [SDL_Window](SDL_Window) that will be the parent of this
  window, required for windows with the "toolip" and "menu" properties
- [`SDL_PROPERTY_WINDOW_CREATE_RESIZABLE_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_RESIZABLE_BOOLEAN)
  ("resizable"): true if the window should be resizable
- [`SDL_PROPERTY_WINDOW_CREATE_TITLE_STRING`](SDL_PROPERTY_WINDOW_CREATE_TITLE_STRING)
  ("title"): the title of the window, in UTF-8 encoding
- [`SDL_PROPERTY_WINDOW_CREATE_TRANSPARENT_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_TRANSPARENT_BOOLEAN)
  ("transparent"): true if the window show transparent in the areas with
  alpha of 0
- [`SDL_PROPERTY_WINDOW_CREATE_TOOLTIP_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_TOOLTIP_BOOLEAN)
  ("tooltip"): true if the window is a tooltip
- [`SDL_PROPERTY_WINDOW_CREATE_UTILITY_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_UTILITY_BOOLEAN)
  ("utility"): true if the window is a utility window, not showing in the
  task bar and window list
- [`SDL_PROPERTY_WINDOW_CREATE_VULKAN_BOOLEAN`](SDL_PROPERTY_WINDOW_CREATE_VULKAN_BOOLEAN)
  ("vulkan"): true if the window will be used with Vulkan rendering
- [`SDL_PROPERTY_WINDOW_CREATE_WIDTH_NUMBER`](SDL_PROPERTY_WINDOW_CREATE_WIDTH_NUMBER)
  ("width"): the width of the window
- [`SDL_PROPERTY_WINDOW_CREATE_X_NUMBER`](SDL_PROPERTY_WINDOW_CREATE_X_NUMBER)
  ("x"): the x position of the window, or
  [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED), defaults to
  [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED). This is relative to
  the parent for windows with the "parent" property set.
- [`SDL_PROPERTY_WINDOW_CREATE_Y_NUMBER`](SDL_PROPERTY_WINDOW_CREATE_Y_NUMBER)
  ("y"): the y position of the window, or
  [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED), defaults to
  [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED). This is relative to
  the parent for windows with the "parent" property set.

These are additional supported properties on macOS:

- [`SDL_PROPERTY_WINDOW_CREATE_COCOA_WINDOW_POINTER`](SDL_PROPERTY_WINDOW_CREATE_COCOA_WINDOW_POINTER)
  ("cocoa.window"): the `(__unsafe_unretained)` NSWindow associated with
  the window, if you want to wrap an existing window.
- [`SDL_PROPERTY_WINDOW_CREATE_COCOA_VIEW_POINTER`](SDL_PROPERTY_WINDOW_CREATE_COCOA_VIEW_POINTER)
  ("cocoa.view"): the `(__unsafe_unretained)` NSView associated with the
  window, defaults to `[window contentView]`

These are additional supported properties on Windows:

- [`SDL_PROPERTY_WINDOW_CREATE_WIN32_HWND_POINTER`](SDL_PROPERTY_WINDOW_CREATE_WIN32_HWND_POINTER)
  ("win32.hwnd"): the HWND associated with the window, if you want to wrap
  an existing window.
- [`SDL_PROPERTY_WINDOW_CREATE_WIN32_PIXEL_FORMAT_HWND_POINTER`](SDL_PROPERTY_WINDOW_CREATE_WIN32_PIXEL_FORMAT_HWND_POINTER)
  ("win32.pixel_format_hwnd"): optional, another window to share pixel
  format with, useful for OpenGL windows

These are additional supported properties with X11:

- [`SDL_PROPERTY_WINDOW_CREATE_X11_WINDOW_NUMBER`](SDL_PROPERTY_WINDOW_CREATE_X11_WINDOW_NUMBER)
  ("x11.window"): the X11 Window associated with the window, if you want to
  wrap an existing window.

The window is implicitly shown if the "hidden" property is not set.

Windows with the "tooltip" and "menu" properties are popup windows and have
the behaviors and guidelines outlined in `SDL_CreatePopupWindow()`.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI)

