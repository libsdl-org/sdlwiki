###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SysWMinfo

The custom window manager information structure.

## Header File

Defined in [SDL_syswm.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_syswm.h)

## Syntax

```c
struct SDL_SysWMinfo
{
    SDL_version version;
    SDL_SYSWM_TYPE subsystem;
    union
    {
#if defined(SDL_VIDEO_DRIVER_WINDOWS)
        struct
        {
            HWND window;                /**< The window handle */
            HDC hdc;                    /**< The window device context */
            HINSTANCE hinstance;        /**< The instance handle */
        } win;
#endif
#if defined(SDL_VIDEO_DRIVER_WINRT)
        struct
        {
            IInspectable * window;      /**< The WinRT CoreWindow */
        } winrt;
#endif
#if defined(SDL_VIDEO_DRIVER_X11)
        struct
        {
            Display *display;           /**< The X11 display */
            Window window;              /**< The X11 window */
        } x11;
#endif
#if defined(SDL_VIDEO_DRIVER_DIRECTFB)
        struct
        {
            IDirectFB *dfb;             /**< The directfb main interface */
            IDirectFBWindow *window;    /**< The directfb window handle */
            IDirectFBSurface *surface;  /**< The directfb client surface */
        } dfb;
#endif
#if defined(SDL_VIDEO_DRIVER_COCOA)
        struct
        {
#if defined(__OBJC__) && defined(__has_feature)
        #if __has_feature(objc_arc)
            NSWindow __unsafe_unretained *window; /**< The Cocoa window */
        #else
            NSWindow *window;                     /**< The Cocoa window */
        #endif
#else
            NSWindow *window;                     /**< The Cocoa window */
#endif
        } cocoa;
#endif
#if defined(SDL_VIDEO_DRIVER_UIKIT)
        struct
        {
#if defined(__OBJC__) && defined(__has_feature)
        #if __has_feature(objc_arc)
            UIWindow __unsafe_unretained *window; /**< The UIKit window */
        #else
            UIWindow *window;                     /**< The UIKit window */
        #endif
#else
            UIWindow *window;                     /**< The UIKit window */
#endif
            GLuint framebuffer; /**< The GL view's Framebuffer Object. It must be bound when rendering to the screen using GL. */
            GLuint colorbuffer; /**< The GL view's color Renderbuffer Object. It must be bound when SDL_GL_SwapWindow is called. */
            GLuint resolveFramebuffer; /**< The Framebuffer Object which holds the resolve color Renderbuffer, when MSAA is used. */
        } uikit;
#endif
#if defined(SDL_VIDEO_DRIVER_WAYLAND)
        struct
        {
            struct wl_display *display;             /**< Wayland display */
            struct wl_surface *surface;             /**< Wayland surface */
            void *shell_surface;                    /**< DEPRECATED Wayland shell_surface (window manager handle) */
            struct wl_egl_window *egl_window;       /**< Wayland EGL window (native window) */
            struct xdg_surface *xdg_surface;        /**< Wayland xdg surface (window manager handle) */
            struct xdg_toplevel *xdg_toplevel;      /**< Wayland xdg toplevel role */
            struct xdg_popup *xdg_popup;            /**< Wayland xdg popup role */
            struct xdg_positioner *xdg_positioner;  /**< Wayland xdg positioner, for popup */
        } wl;
#endif
#if defined(SDL_VIDEO_DRIVER_MIR)  /* no longer available, left for API/ABI compatibility. Remove in 2.1! */
        struct
        {
            void *connection;  /**< Mir display server connection */
            void *surface;  /**< Mir surface */
        } mir;
#endif

#if defined(SDL_VIDEO_DRIVER_ANDROID)
        struct
        {
            ANativeWindow *window;
            EGLSurface surface;
        } android;
#endif

#if defined(SDL_VIDEO_DRIVER_OS2)
        struct
        {
            HWND hwnd;                  /**< The window handle */
            HWND hwndFrame;             /**< The frame window handle */
        } os2;
#endif

#if defined(SDL_VIDEO_DRIVER_VIVANTE)
        struct
        {
            EGLNativeDisplayType display;
            EGLNativeWindowType window;
        } vivante;
#endif

#if defined(SDL_VIDEO_DRIVER_KMSDRM)
        struct
        {
            int dev_index;               /**< Device index (ex: the X in /dev/dri/cardX) */
            int drm_fd;                  /**< DRM FD (unavailable on Vulkan windows) */
            struct gbm_device *gbm_dev;  /**< GBM device (unavailable on Vulkan windows) */
        } kmsdrm;
#endif

        /* Make sure this union is always 64 bytes (8 64-bit pointers). */
        /* Be careful not to overflow this if you add a new target! */
        Uint8 dummy[64];
    } info;
};
```

## Remarks

When this structure is returned, it holds information about which low level
system it is using, and will be one of [SDL_SYSWM_TYPE](SDL_SYSWM_TYPE).

## Data Fields

{|
|
|
| style="background-color: #EDEDED;" | ''All Subsystems''
|-
|[SDL_version](SDL_version)
|'''version'''
|an [SDL_version](SDL_version) structure that contains the current SDL version
|-
|[SDL_SYSWM_TYPE](SDL_SYSWM_TYPE)
|'''subsystem'''
|the windowing system type; see Remarks for details
|-
| style="color: #808080;" | int
| style="color: #808080;" | '''dummy'''
| style="color: #808080;" | unused (to help compilers when no specific system is available)
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_WINDOWS''
|-
|HWND
|'''win.window'''
|the window handle
|-
|HDC 
|'''win.hdc'''   
|the window device context (>= SDL 2.0.4)
|-
|HINSTANCE 
|'''win.hinstance'''   
|the window hinstance (>= SDL 2.0.6)
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_WINRT'' (>= SDL 2.0.3)
|-
|IInspectable*
|'''winrt.window'''
|the WinRT CoreWindow
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_X11''
|-
|Display*
|'''x11.display'''
|the X11 display
|-
|Window
|'''x11.window'''
|the X11 window
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_DIRECTFB''
|-
|IDirectFB*
|'''dfb.dfb'''
|the DirectFB main interface
|-
|IDirectFBWindow*
|'''dfb.window'''
|the DirectFB window handle
|-
|IDirectFBSurface*
|'''dfb.surface'''
|the DirectFB client surface
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_COCOA''
|-
|NSWindow*
|'''cocoa.window'''
|the Cocoa window
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_UIKIT''
|-
|UIWindow*
|'''uikit.window'''
|the UIKit window
|-
|GLuint   
|'''uikit.framebuffer''' 
|the GL view's Framebuffer Object; it must be bound when rendering to the screen using GL (>= SDL 2.0.4)
|-
|GLuint   
|'''uikit.colorbuffer''' 
|the GL view's color Renderbuffer Object; it must be bound when [SDL_GL_SwapWindow](SDL_GL_SwapWindow)() is called (>= SDL 2.0.4)
|-
|GLuint   
|'''uikit.resolveFramebuffer''' 
|the Framebuffer Object which holds the resolve color Renderbuffer, when MSAA is used (>= SDL 2.0.4)
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_WAYLAND'' (>= SDL 2.0.2)
|-
|wl_display*
|'''wl.display'''
|the Wayland display
|-
|wl_surface*
|'''wl.surface'''
|the Wayland surface
|-
|wl_shell_surface*
|'''wl.shell_surface'''
|the Wayland shell_surface (window manager handle)
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_MIR'' (>= SDL 2.0.2)
|-
|MirConnection*
|'''mir.connection'''
|the Mir display server connection
|-
|MirSurface*
|'''mir.surface'''
|the Mir surface
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_ANDROID'' (>= SDL 2.0.4)
|-
|ANativeWindow*
|'''android.window'''
|the Android native window
|-
|EGLSurface
|'''android.surface'''
|the Android EGL surface
|-
|
|
| style="background-color: #EDEDED;" | ''SDL_SYSWM_VIVANTE'' (>= SDL 2.0.5)
|-
|EGLNativeDisplayType
|'''vivante.display'''
|the Vivante EGL display type
|-
|EGLNativeWindowType
|'''vivante.window'''
|the Vivante EGL window type
|}

## Related Enumerations

[SDL_SYSWM_TYPE](SDL_SYSWM_TYPE)

## Related Structures

[SDL_version](SDL_version)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategorySWM](CategorySWM)


