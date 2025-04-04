# CategoryVideo

SDL's video subsystem is largely interested in abstracting window
management from the underlying operating system. You can create windows,
manage them in various ways, set them fullscreen, and get events when
interesting things happen with them, such as the mouse or keyboard
interacting with a window.

The video subsystem is also interested in abstracting away some
platform-specific differences in OpenGL: context creation, swapping
buffers, etc. This may be crucial to your app, but also you are not
required to use OpenGL at all. In fact, SDL can provide rendering to those
windows as well, either with an easy-to-use
[2D API](https://wiki.libsdl.org/SDL3/CategoryRender)
or with a more-powerful
[GPU API](https://wiki.libsdl.org/SDL3/CategoryGPU)
. Of course, it can simply get out of your way and give you the window
handles you need to use Vulkan, Direct3D, Metal, or whatever else you like
directly, too.

The video subsystem covers a lot of functionality, out of necessity, so it
is worth perusing the list of functions just to see what's available, but
most apps can get by with simply creating a window and listening for
events, so start with [SDL_CreateWindow](SDL_CreateWindow)() and
[SDL_PollEvent](SDL_PollEvent)().

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryVideo, CategoryAPIFunction -->
- [SDL_CreatePopupWindow](SDL_CreatePopupWindow)
- [SDL_CreateWindow](SDL_CreateWindow)
- [SDL_CreateWindowWithProperties](SDL_CreateWindowWithProperties)
- [SDL_DestroyWindow](SDL_DestroyWindow)
- [SDL_DestroyWindowSurface](SDL_DestroyWindowSurface)
- [SDL_DisableScreenSaver](SDL_DisableScreenSaver)
- [SDL_EGL_GetCurrentConfig](SDL_EGL_GetCurrentConfig)
- [SDL_EGL_GetCurrentDisplay](SDL_EGL_GetCurrentDisplay)
- [SDL_EGL_GetProcAddress](SDL_EGL_GetProcAddress)
- [SDL_EGL_GetWindowSurface](SDL_EGL_GetWindowSurface)
- [SDL_EGL_SetAttributeCallbacks](SDL_EGL_SetAttributeCallbacks)
- [SDL_EnableScreenSaver](SDL_EnableScreenSaver)
- [SDL_FlashWindow](SDL_FlashWindow)
- [SDL_GetClosestFullscreenDisplayMode](SDL_GetClosestFullscreenDisplayMode)
- [SDL_GetCurrentDisplayMode](SDL_GetCurrentDisplayMode)
- [SDL_GetCurrentDisplayOrientation](SDL_GetCurrentDisplayOrientation)
- [SDL_GetCurrentVideoDriver](SDL_GetCurrentVideoDriver)
- [SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode)
- [SDL_GetDisplayBounds](SDL_GetDisplayBounds)
- [SDL_GetDisplayContentScale](SDL_GetDisplayContentScale)
- [SDL_GetDisplayForPoint](SDL_GetDisplayForPoint)
- [SDL_GetDisplayForRect](SDL_GetDisplayForRect)
- [SDL_GetDisplayForWindow](SDL_GetDisplayForWindow)
- [SDL_GetDisplayName](SDL_GetDisplayName)
- [SDL_GetDisplayProperties](SDL_GetDisplayProperties)
- [SDL_GetDisplays](SDL_GetDisplays)
- [SDL_GetDisplayUsableBounds](SDL_GetDisplayUsableBounds)
- [SDL_GetFullscreenDisplayModes](SDL_GetFullscreenDisplayModes)
- [SDL_GetGrabbedWindow](SDL_GetGrabbedWindow)
- [SDL_GetNaturalDisplayOrientation](SDL_GetNaturalDisplayOrientation)
- [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers)
- [SDL_GetPrimaryDisplay](SDL_GetPrimaryDisplay)
- [SDL_GetSystemTheme](SDL_GetSystemTheme)
- [SDL_GetVideoDriver](SDL_GetVideoDriver)
- [SDL_GetWindowAspectRatio](SDL_GetWindowAspectRatio)
- [SDL_GetWindowBordersSize](SDL_GetWindowBordersSize)
- [SDL_GetWindowDisplayScale](SDL_GetWindowDisplayScale)
- [SDL_GetWindowFlags](SDL_GetWindowFlags)
- [SDL_GetWindowFromID](SDL_GetWindowFromID)
- [SDL_GetWindowFullscreenMode](SDL_GetWindowFullscreenMode)
- [SDL_GetWindowICCProfile](SDL_GetWindowICCProfile)
- [SDL_GetWindowID](SDL_GetWindowID)
- [SDL_GetWindowKeyboardGrab](SDL_GetWindowKeyboardGrab)
- [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize)
- [SDL_GetWindowMinimumSize](SDL_GetWindowMinimumSize)
- [SDL_GetWindowMouseGrab](SDL_GetWindowMouseGrab)
- [SDL_GetWindowMouseRect](SDL_GetWindowMouseRect)
- [SDL_GetWindowOpacity](SDL_GetWindowOpacity)
- [SDL_GetWindowParent](SDL_GetWindowParent)
- [SDL_GetWindowPixelDensity](SDL_GetWindowPixelDensity)
- [SDL_GetWindowPixelFormat](SDL_GetWindowPixelFormat)
- [SDL_GetWindowPosition](SDL_GetWindowPosition)
- [SDL_GetWindowProgressState](SDL_GetWindowProgressState)
- [SDL_GetWindowProgressValue](SDL_GetWindowProgressValue)
- [SDL_GetWindowProperties](SDL_GetWindowProperties)
- [SDL_GetWindows](SDL_GetWindows)
- [SDL_GetWindowSafeArea](SDL_GetWindowSafeArea)
- [SDL_GetWindowSize](SDL_GetWindowSize)
- [SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels)
- [SDL_GetWindowSurface](SDL_GetWindowSurface)
- [SDL_GetWindowSurfaceVSync](SDL_GetWindowSurfaceVSync)
- [SDL_GetWindowTitle](SDL_GetWindowTitle)
- [SDL_GL_CreateContext](SDL_GL_CreateContext)
- [SDL_GL_DestroyContext](SDL_GL_DestroyContext)
- [SDL_GL_ExtensionSupported](SDL_GL_ExtensionSupported)
- [SDL_GL_GetAttribute](SDL_GL_GetAttribute)
- [SDL_GL_GetCurrentContext](SDL_GL_GetCurrentContext)
- [SDL_GL_GetCurrentWindow](SDL_GL_GetCurrentWindow)
- [SDL_GL_GetProcAddress](SDL_GL_GetProcAddress)
- [SDL_GL_GetSwapInterval](SDL_GL_GetSwapInterval)
- [SDL_GL_LoadLibrary](SDL_GL_LoadLibrary)
- [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent)
- [SDL_GL_ResetAttributes](SDL_GL_ResetAttributes)
- [SDL_GL_SetAttribute](SDL_GL_SetAttribute)
- [SDL_GL_SetSwapInterval](SDL_GL_SetSwapInterval)
- [SDL_GL_SwapWindow](SDL_GL_SwapWindow)
- [SDL_GL_UnloadLibrary](SDL_GL_UnloadLibrary)
- [SDL_HideWindow](SDL_HideWindow)
- [SDL_MaximizeWindow](SDL_MaximizeWindow)
- [SDL_MinimizeWindow](SDL_MinimizeWindow)
- [SDL_RaiseWindow](SDL_RaiseWindow)
- [SDL_RestoreWindow](SDL_RestoreWindow)
- [SDL_ScreenSaverEnabled](SDL_ScreenSaverEnabled)
- [SDL_SetWindowAlwaysOnTop](SDL_SetWindowAlwaysOnTop)
- [SDL_SetWindowAspectRatio](SDL_SetWindowAspectRatio)
- [SDL_SetWindowBordered](SDL_SetWindowBordered)
- [SDL_SetWindowFocusable](SDL_SetWindowFocusable)
- [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)
- [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)
- [SDL_SetWindowHitTest](SDL_SetWindowHitTest)
- [SDL_SetWindowIcon](SDL_SetWindowIcon)
- [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab)
- [SDL_SetWindowMaximumSize](SDL_SetWindowMaximumSize)
- [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize)
- [SDL_SetWindowModal](SDL_SetWindowModal)
- [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)
- [SDL_SetWindowMouseRect](SDL_SetWindowMouseRect)
- [SDL_SetWindowOpacity](SDL_SetWindowOpacity)
- [SDL_SetWindowParent](SDL_SetWindowParent)
- [SDL_SetWindowPosition](SDL_SetWindowPosition)
- [SDL_SetWindowProgressState](SDL_SetWindowProgressState)
- [SDL_SetWindowProgressValue](SDL_SetWindowProgressValue)
- [SDL_SetWindowResizable](SDL_SetWindowResizable)
- [SDL_SetWindowShape](SDL_SetWindowShape)
- [SDL_SetWindowSize](SDL_SetWindowSize)
- [SDL_SetWindowSurfaceVSync](SDL_SetWindowSurfaceVSync)
- [SDL_SetWindowTitle](SDL_SetWindowTitle)
- [SDL_ShowWindow](SDL_ShowWindow)
- [SDL_ShowWindowSystemMenu](SDL_ShowWindowSystemMenu)
- [SDL_SyncWindow](SDL_SyncWindow)
- [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface)
- [SDL_UpdateWindowSurfaceRects](SDL_UpdateWindowSurfaceRects)
- [SDL_WindowHasSurface](SDL_WindowHasSurface)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryVideo, CategoryAPIDatatype -->
- [SDL_DisplayID](SDL_DisplayID)
- [SDL_DisplayModeData](SDL_DisplayModeData)
- [SDL_EGLAttrib](SDL_EGLAttrib)
- [SDL_EGLAttribArrayCallback](SDL_EGLAttribArrayCallback)
- [SDL_EGLConfig](SDL_EGLConfig)
- [SDL_EGLDisplay](SDL_EGLDisplay)
- [SDL_EGLint](SDL_EGLint)
- [SDL_EGLIntArrayCallback](SDL_EGLIntArrayCallback)
- [SDL_EGLSurface](SDL_EGLSurface)
- [SDL_GLContext](SDL_GLContext)
- [SDL_GLContextFlag](SDL_GLContextFlag)
- [SDL_GLContextReleaseFlag](SDL_GLContextReleaseFlag)
- [SDL_GLContextResetNotification](SDL_GLContextResetNotification)
- [SDL_GLProfile](SDL_GLProfile)
- [SDL_HitTest](SDL_HitTest)
- [SDL_Window](SDL_Window)
- [SDL_WindowFlags](SDL_WindowFlags)
- [SDL_WindowID](SDL_WindowID)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryVideo, CategoryAPIStruct -->
- [SDL_DisplayMode](SDL_DisplayMode)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryVideo, CategoryAPIEnum -->
- [SDL_DisplayOrientation](SDL_DisplayOrientation)
- [SDL_FlashOperation](SDL_FlashOperation)
- [SDL_GLAttr](SDL_GLAttr)
- [SDL_HitTestResult](SDL_HitTestResult)
- [SDL_ProgressState](SDL_ProgressState)
- [SDL_SystemTheme](SDL_SystemTheme)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryVideo, CategoryAPIMacro -->
- [SDL_PROP_GLOBAL_VIDEO_WAYLAND_WL_DISPLAY_POINTER](SDL_PROP_GLOBAL_VIDEO_WAYLAND_WL_DISPLAY_POINTER)
- [SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED)
- [SDL_WINDOWPOS_CENTERED_DISPLAY](SDL_WINDOWPOS_CENTERED_DISPLAY)
- [SDL_WINDOWPOS_CENTERED_MASK](SDL_WINDOWPOS_CENTERED_MASK)
- [SDL_WINDOWPOS_ISCENTERED](SDL_WINDOWPOS_ISCENTERED)
- [SDL_WINDOWPOS_ISUNDEFINED](SDL_WINDOWPOS_ISUNDEFINED)
- [SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED)
- [SDL_WINDOWPOS_UNDEFINED_DISPLAY](SDL_WINDOWPOS_UNDEFINED_DISPLAY)
- [SDL_WINDOWPOS_UNDEFINED_MASK](SDL_WINDOWPOS_UNDEFINED_MASK)
<!-- END CATEGORY LIST -->


----
[CategoryAPICategory](CategoryAPICategory)

