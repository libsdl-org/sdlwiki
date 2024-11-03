###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CreateWindowWithProperties

Create a window with the specified properties.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_Window * SDL_CreateWindowWithProperties(SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                        |
| ------------------------------------ | --------- | ---------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to use. |

## Return Value

([SDL_Window](SDL_Window) *) Returns the window that was created or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

These are the supported properties:

- [`SDL_PROP_WINDOW_CREATE_ALWAYS_ON_TOP_BOOLEAN`](SDL_PROP_WINDOW_CREATE_ALWAYS_ON_TOP_BOOLEAN):
  true if the window should be always on top
- [`SDL_PROP_WINDOW_CREATE_BORDERLESS_BOOLEAN`](SDL_PROP_WINDOW_CREATE_BORDERLESS_BOOLEAN):
  true if the window has no window decoration
- [`SDL_PROP_WINDOW_CREATE_EXTERNAL_GRAPHICS_CONTEXT_BOOLEAN`](SDL_PROP_WINDOW_CREATE_EXTERNAL_GRAPHICS_CONTEXT_BOOLEAN):
  true if the window will be used with an externally managed graphics
  context.
- [`SDL_PROP_WINDOW_CREATE_FOCUSABLE_BOOLEAN`](SDL_PROP_WINDOW_CREATE_FOCUSABLE_BOOLEAN):
  true if the window should accept keyboard input (defaults true)
- [`SDL_PROP_WINDOW_CREATE_FULLSCREEN_BOOLEAN`](SDL_PROP_WINDOW_CREATE_FULLSCREEN_BOOLEAN):
  true if the window should start in fullscreen mode at desktop resolution
- [`SDL_PROP_WINDOW_CREATE_HEIGHT_NUMBER`](SDL_PROP_WINDOW_CREATE_HEIGHT_NUMBER):
  the height of the window
- [`SDL_PROP_WINDOW_CREATE_HIDDEN_BOOLEAN`](SDL_PROP_WINDOW_CREATE_HIDDEN_BOOLEAN):
  true if the window should start hidden
- [`SDL_PROP_WINDOW_CREATE_HIGH_PIXEL_DENSITY_BOOLEAN`](SDL_PROP_WINDOW_CREATE_HIGH_PIXEL_DENSITY_BOOLEAN):
  true if the window uses a high pixel density buffer if possible
- [`SDL_PROP_WINDOW_CREATE_MAXIMIZED_BOOLEAN`](SDL_PROP_WINDOW_CREATE_MAXIMIZED_BOOLEAN):
  true if the window should start maximized
- [`SDL_PROP_WINDOW_CREATE_MENU_BOOLEAN`](SDL_PROP_WINDOW_CREATE_MENU_BOOLEAN):
  true if the window is a popup menu
- [`SDL_PROP_WINDOW_CREATE_METAL_BOOLEAN`](SDL_PROP_WINDOW_CREATE_METAL_BOOLEAN):
  true if the window will be used with Metal rendering
- [`SDL_PROP_WINDOW_CREATE_MINIMIZED_BOOLEAN`](SDL_PROP_WINDOW_CREATE_MINIMIZED_BOOLEAN):
  true if the window should start minimized
- [`SDL_PROP_WINDOW_CREATE_MODAL_BOOLEAN`](SDL_PROP_WINDOW_CREATE_MODAL_BOOLEAN):
  true if the window is modal to its parent
- [`SDL_PROP_WINDOW_CREATE_MOUSE_GRABBED_BOOLEAN`](SDL_PROP_WINDOW_CREATE_MOUSE_GRABBED_BOOLEAN):
  true if the window starts with grabbed mouse focus
- [`SDL_PROP_WINDOW_CREATE_OPENGL_BOOLEAN`](SDL_PROP_WINDOW_CREATE_OPENGL_BOOLEAN):
  true if the window will be used with OpenGL rendering
- [`SDL_PROP_WINDOW_CREATE_PARENT_POINTER`](SDL_PROP_WINDOW_CREATE_PARENT_POINTER):
  an [SDL_Window](SDL_Window) that will be the parent of this window,
  required for windows with the "tooltip", "menu", and "modal" properties
- [`SDL_PROP_WINDOW_CREATE_RESIZABLE_BOOLEAN`](SDL_PROP_WINDOW_CREATE_RESIZABLE_BOOLEAN):
  true if the window should be resizable
- [`SDL_PROP_WINDOW_CREATE_TITLE_STRING`](SDL_PROP_WINDOW_CREATE_TITLE_STRING):
  the title of the window, in UTF-8 encoding
- [`SDL_PROP_WINDOW_CREATE_TRANSPARENT_BOOLEAN`](SDL_PROP_WINDOW_CREATE_TRANSPARENT_BOOLEAN):
  true if the window show transparent in the areas with alpha of 0
- [`SDL_PROP_WINDOW_CREATE_TOOLTIP_BOOLEAN`](SDL_PROP_WINDOW_CREATE_TOOLTIP_BOOLEAN):
  true if the window is a tooltip
- [`SDL_PROP_WINDOW_CREATE_UTILITY_BOOLEAN`](SDL_PROP_WINDOW_CREATE_UTILITY_BOOLEAN):
  true if the window is a utility window, not showing in the task bar and
  window list
- [`SDL_PROP_WINDOW_CREATE_VULKAN_BOOLEAN`](SDL_PROP_WINDOW_CREATE_VULKAN_BOOLEAN):
  true if the window will be used with Vulkan rendering
- [`SDL_PROP_WINDOW_CREATE_WIDTH_NUMBER`](SDL_PROP_WINDOW_CREATE_WIDTH_NUMBER):
  the width of the window
- [`SDL_PROP_WINDOW_CREATE_X_NUMBER`](SDL_PROP_WINDOW_CREATE_X_NUMBER): the
  x position of the window, or
  [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED), defaults to
  [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED). This is relative to
  the parent for windows with the "parent" property set.
- [`SDL_PROP_WINDOW_CREATE_Y_NUMBER`](SDL_PROP_WINDOW_CREATE_Y_NUMBER): the
  y position of the window, or
  [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED), defaults to
  [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED). This is relative to
  the parent for windows with the "parent" property set.

These are additional supported properties on macOS:

- [`SDL_PROP_WINDOW_CREATE_COCOA_WINDOW_POINTER`](SDL_PROP_WINDOW_CREATE_COCOA_WINDOW_POINTER):
  the `(__unsafe_unretained)` NSWindow associated with the window, if you
  want to wrap an existing window.
- [`SDL_PROP_WINDOW_CREATE_COCOA_VIEW_POINTER`](SDL_PROP_WINDOW_CREATE_COCOA_VIEW_POINTER):
  the `(__unsafe_unretained)` NSView associated with the window, defaults
  to `[window contentView]`

These are additional supported properties on Wayland:

- [`SDL_PROP_WINDOW_CREATE_WAYLAND_SURFACE_ROLE_CUSTOM_BOOLEAN`](SDL_PROP_WINDOW_CREATE_WAYLAND_SURFACE_ROLE_CUSTOM_BOOLEAN)
  - true if the application wants to use the Wayland surface for a custom
  role and does not want it attached to an XDG toplevel window. See
  [README/wayland](README/wayland) for more information on using custom
  surfaces.
- [`SDL_PROP_WINDOW_CREATE_WAYLAND_CREATE_EGL_WINDOW_BOOLEAN`](SDL_PROP_WINDOW_CREATE_WAYLAND_CREATE_EGL_WINDOW_BOOLEAN)
  - true if the application wants an associated `wl_egl_window` object to
  be created and attached to the window, even if the window does not have
  the OpenGL property or [`SDL_WINDOW_OPENGL`](SDL_WINDOW_OPENGL) flag set.
- [`SDL_PROP_WINDOW_CREATE_WAYLAND_WL_SURFACE_POINTER`](SDL_PROP_WINDOW_CREATE_WAYLAND_WL_SURFACE_POINTER)
  - the wl_surface associated with the window, if you want to wrap an
  existing window. See [README/wayland](README/wayland) for more
  information.

These are additional supported properties on Windows:

- [`SDL_PROP_WINDOW_CREATE_WIN32_HWND_POINTER`](SDL_PROP_WINDOW_CREATE_WIN32_HWND_POINTER):
  the HWND associated with the window, if you want to wrap an existing
  window.
- [`SDL_PROP_WINDOW_CREATE_WIN32_PIXEL_FORMAT_HWND_POINTER`](SDL_PROP_WINDOW_CREATE_WIN32_PIXEL_FORMAT_HWND_POINTER):
  optional, another window to share pixel format with, useful for OpenGL
  windows

These are additional supported properties with X11:

- [`SDL_PROP_WINDOW_CREATE_X11_WINDOW_NUMBER`](SDL_PROP_WINDOW_CREATE_X11_WINDOW_NUMBER):
  the X11 Window associated with the window, if you want to wrap an
  existing window.

The window is implicitly shown if the "hidden" property is not set.

Windows with the "tooltip" and "menu" properties are popup windows and have
the behaviors and guidelines outlined in
[SDL_CreatePopupWindow](SDL_CreatePopupWindow)().

If this window is being created to be used with an
[SDL_Renderer](SDL_Renderer), you should not add a graphics API specific
property
([`SDL_PROP_WINDOW_CREATE_OPENGL_BOOLEAN`](SDL_PROP_WINDOW_CREATE_OPENGL_BOOLEAN),
etc), as SDL will handle that internally when it chooses a renderer.
However, SDL might need to recreate your window at that point, which may
cause the window to appear briefly, and then flicker as it is recreated.
The correct approach to this is to create the window with the
[`SDL_PROP_WINDOW_CREATE_HIDDEN_BOOLEAN`](SDL_PROP_WINDOW_CREATE_HIDDEN_BOOLEAN)
property set to true, then create the renderer, then show the window with
[SDL_ShowWindow](SDL_ShowWindow)().

## Version

This function is available since SDL 3.1.3.

## Code Examples

```c
// Example program
// Use SDL3 to create a window with properties

#include <SDL3/SDL_log.h>
#include <SDL3/SDL_main.h>
#include <SDL3/SDL_video.h>

int
main(int argc, char** argv)
{
  if (!SDL_Init(SDL_INIT_VIDEO)) {
    SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
    return 0;
  }

  SDL_PropertiesID props = SDL_CreateProperties();
  if(props == 0) {
    SDL_Log("Unable to create properties: %s", SDL_GetError());
    return 0;
  }

  // Assume the following calls succeed
  SDL_SetStringProperty(props, SDL_PROP_WINDOW_CREATE_TITLE_STRING, "My Window");
  SDL_SetBooleanProperty(props, SDL_PROP_WINDOW_CREATE_RESIZABLE_BOOLEAN, true);
  SDL_SetNumberProperty(props, SDL_PROP_WINDOW_CREATE_WIDTH_NUMBER, 640);
  SDL_SetNumberProperty(props, SDL_PROP_WINDOW_CREATE_HEIGHT_NUMBER, 480);

  SDL_Window *window = SDL_CreateWindowWithProperties(props);
  if(window == NULL) {
    SDL_Log("Unable to create window: %s", SDL_GetError());
    return 0;
  }

  // A game loop goes here

  SDL_DestroyWindow(window);
  SDL_DestroyProperties(props);

  return 0;
}
```

## See Also

- [SDL_CreateProperties](SDL_CreateProperties)
- [SDL_CreateWindow](SDL_CreateWindow)
- [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

