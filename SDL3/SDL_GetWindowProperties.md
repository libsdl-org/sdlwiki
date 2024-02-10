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

The following read-only properties are provided by SDL:

- [`SDL_PROP_WINDOW_SHAPE_POINTER`](SDL_PROP_WINDOW_SHAPE_POINTER): the
  surface associated with a shaped window

On Android:

- [`SDL_PROP_WINDOW_ANDROID_WINDOW_POINTER`](SDL_PROP_WINDOW_ANDROID_WINDOW_POINTER):
  the ANativeWindow associated with the window
- [`SDL_PROP_WINDOW_ANDROID_SURFACE_POINTER`](SDL_PROP_WINDOW_ANDROID_SURFACE_POINTER):
  the EGLSurface associated with the window

On iOS:

- [`SDL_PROP_WINDOW_UIKIT_WINDOW_POINTER`](SDL_PROP_WINDOW_UIKIT_WINDOW_POINTER):
  the `(__unsafe_unretained)` UIWindow associated with the window
- [`SDL_PROP_WINDOW_UIKIT_METAL_VIEW_TAG_NUMBER`](SDL_PROP_WINDOW_UIKIT_METAL_VIEW_TAG_NUMBER):
  the NSInteger tag assocated with metal views on the window

On KMS/DRM:

- [`SDL_PROP_WINDOW_KMSDRM_DEVICE_INDEX_NUMBER`](SDL_PROP_WINDOW_KMSDRM_DEVICE_INDEX_NUMBER):
  the device index associated with the window (e.g. the X in
  /dev/dri/cardX)
- [`SDL_PROP_WINDOW_KMSDRM_DRM_FD_NUMBER`](SDL_PROP_WINDOW_KMSDRM_DRM_FD_NUMBER):
  the DRM FD associated with the window
- [`SDL_PROP_WINDOW_KMSDRM_GBM_DEVICE_POINTER`](SDL_PROP_WINDOW_KMSDRM_GBM_DEVICE_POINTER):
  the GBM device associated with the window

On macOS:

- [`SDL_PROP_WINDOW_COCOA_WINDOW_POINTER`](SDL_PROP_WINDOW_COCOA_WINDOW_POINTER):
  the `(__unsafe_unretained)` NSWindow associated with the window
- [`SDL_PROP_WINDOW_COCOA_METAL_VIEW_TAG_NUMBER`](SDL_PROP_WINDOW_COCOA_METAL_VIEW_TAG_NUMBER):
  the NSInteger tag assocated with metal views on the window

On Vivante:

- [`SDL_PROP_WINDOW_VIVANTE_DISPLAY_POINTER`](SDL_PROP_WINDOW_VIVANTE_DISPLAY_POINTER):
  the EGLNativeDisplayType associated with the window
- [`SDL_PROP_WINDOW_VIVANTE_WINDOW_POINTER`](SDL_PROP_WINDOW_VIVANTE_WINDOW_POINTER):
  the EGLNativeWindowType associated with the window
- [`SDL_PROP_WINDOW_VIVANTE_SURFACE_POINTER`](SDL_PROP_WINDOW_VIVANTE_SURFACE_POINTER):
  the EGLSurface associated with the window

On UWP:

- [`SDL_PROP_WINDOW_WINRT_WINDOW_POINTER`](SDL_PROP_WINDOW_WINRT_WINDOW_POINTER):
  the IInspectable CoreWindow associated with the window

On Windows:

- [`SDL_PROP_WINDOW_WIN32_HWND_POINTER`](SDL_PROP_WINDOW_WIN32_HWND_POINTER):
  the HWND associated with the window
- [`SDL_PROP_WINDOW_WIN32_HDC_POINTER`](SDL_PROP_WINDOW_WIN32_HDC_POINTER):
  the HDC associated with the window
- [`SDL_PROP_WINDOW_WIN32_INSTANCE_POINTER`](SDL_PROP_WINDOW_WIN32_INSTANCE_POINTER):
  the HINSTANCE associated with the window

On Wayland:

Note: The `xdg_*` window objects do not internally persist across window
show/hide calls. They will be null if the window is hidden and must be
queried each time it is shown.

- [`SDL_PROP_WINDOW_WAYLAND_DISPLAY_POINTER`](SDL_PROP_WINDOW_WAYLAND_DISPLAY_POINTER):
  the wl_display associated with the window
- [`SDL_PROP_WINDOW_WAYLAND_SURFACE_POINTER`](SDL_PROP_WINDOW_WAYLAND_SURFACE_POINTER):
  the wl_surface associated with the window
- [`SDL_PROP_WINDOW_WAYLAND_EGL_WINDOW_POINTER`](SDL_PROP_WINDOW_WAYLAND_EGL_WINDOW_POINTER):
  the wl_egl_window associated with the window
- [`SDL_PROP_WINDOW_WAYLAND_XDG_SURFACE_POINTER`](SDL_PROP_WINDOW_WAYLAND_XDG_SURFACE_POINTER):
  the xdg_surface associated with the window
- [`SDL_PROP_WINDOW_WAYLAND_XDG_TOPLEVEL_POINTER`](SDL_PROP_WINDOW_WAYLAND_XDG_TOPLEVEL_POINTER):
  the xdg_toplevel role associated with the window
- [`SDL_PROP_WINDOW_WAYLAND_XDG_POPUP_POINTER`](SDL_PROP_WINDOW_WAYLAND_XDG_POPUP_POINTER):
  the xdg_popup role associated with the window
- [`SDL_PROP_WINDOW_WAYLAND_XDG_POSITIONER_POINTER`](SDL_PROP_WINDOW_WAYLAND_XDG_POSITIONER_POINTER):
  the xdg_positioner associated with the window, in popup mode

On X11:

- [`SDL_PROP_WINDOW_X11_DISPLAY_POINTER`](SDL_PROP_WINDOW_X11_DISPLAY_POINTER):
  the X11 Display associated with the window
- [`SDL_PROP_WINDOW_X11_SCREEN_NUMBER`](SDL_PROP_WINDOW_X11_SCREEN_NUMBER):
  the screen number associated with the window
- [`SDL_PROP_WINDOW_X11_WINDOW_NUMBER`](SDL_PROP_WINDOW_X11_WINDOW_NUMBER):
  the X11 Window associated with the window

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

