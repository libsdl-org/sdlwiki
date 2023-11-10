###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowProperties

Get the properties associated with a window.

## Syntax

```c
SDL_PropertiesID SDL_GetWindowProperties(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The following properties are provided by SDL:

On Android: "SDL.window.android.window" - the ANativeWindow associated with
the window "SDL.window.android.surface" - the EGLSurface associated with
the window

On iOS: "SDL.window.uikit.window" - the (__unsafe_unretained) UIWindow
associated with the window "SDL.window.uikit.metal_view_tag" - the
NSInteger tag assocated with metal views on the window

On KMS/DRM: "SDL.window.kmsdrm.dev_index" - the device index associated
with the window (e.g. the X in /dev/dri/cardX) "SDL.window.kmsdrm.drm_fd" -
the DRM FD associated with the window "SDL.window.kmsdrm.gbm_dev" - the GBM
device associated with the window

On macOS: "SDL.window.cocoa.window" - the (__unsafe_unretained) NSWindow
associated with the window "SDL.window.cocoa.metal_view_tag" - the
NSInteger tag assocated with metal views on the window

On Vivante: "SDL.window.vivante.display" - the EGLNativeDisplayType
associated with the window "SDL.window.vivante.window" - the
EGLNativeWindowType associated with the window "SDL.window.vivante.surface"
- the EGLSurface associated with the window

On UWP: "SDL.window.winrt.window" - the IInspectable CoreWindow associated
with the window

On Windows: "SDL.window.win32.hwnd" - the HWND associated with the window
"SDL.window.win32.hdc" - the HDC associated with the window
"SDL.window.win32.instance" - the HINSTANCE associated with the window

On Wayland: "SDL.window.wayland.registry" - the wl_registry associated with
the window "SDL.window.wayland.display" - the wl_display associated with
the window "SDL.window.wayland.surface" - the wl_surface associated with
the window "SDL.window.wayland.egl_window" - the wl_egl_window associated
with the window "SDL.window.wayland.xdg_surface" - the xdg_surface
associated with the window "SDL.window.wayland.xdg_toplevel" - the
xdg_toplevel role associated with the window "SDL.window.wayland.xdg_popup"
- the xdg_popup role associated with the window
"SDL.window.wayland.xdg_positioner" - the xdg_positioner associated with
the window, in popup mode

Note: The xdg_* window objects do not internally persist across window
show/hide calls. They will be null if the window is hidden and must be
queried each time it is shown.

On X11: "SDL.window.x11.display" - the X11 Display associated with the
window "SDL.window.x11.screen" - the screen number associated with the
window "SDL.window.x11.window" - the X11 Window associated with the window

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

