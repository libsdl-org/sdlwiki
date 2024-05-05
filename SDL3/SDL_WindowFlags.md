###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WindowFlags

The flags on a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef Uint32 SDL_WindowFlags;

#define SDL_WINDOW_FULLSCREEN           0x00000001U /**< window is in fullscreen mode */
#define SDL_WINDOW_OPENGL               0x00000002U /**< window usable with OpenGL context */
#define SDL_WINDOW_OCCLUDED             0x00000004U /**< window is occluded */
#define SDL_WINDOW_HIDDEN               0x00000008U /**< window is neither mapped onto the desktop nor shown in the taskbar/dock/window list; SDL_ShowWindow() is required for it to become visible */
#define SDL_WINDOW_BORDERLESS           0x00000010U /**< no window decoration */
#define SDL_WINDOW_RESIZABLE            0x00000020U /**< window can be resized */
#define SDL_WINDOW_MINIMIZED            0x00000040U /**< window is minimized */
#define SDL_WINDOW_MAXIMIZED            0x00000080U /**< window is maximized */
#define SDL_WINDOW_MOUSE_GRABBED        0x00000100U /**< window has grabbed mouse input */
#define SDL_WINDOW_INPUT_FOCUS          0x00000200U /**< window has input focus */
#define SDL_WINDOW_MOUSE_FOCUS          0x00000400U /**< window has mouse focus */
#define SDL_WINDOW_EXTERNAL             0x00000800U /**< window not created by SDL */
#define SDL_WINDOW_MODAL                0x00001000U /**< window is modal */
#define SDL_WINDOW_HIGH_PIXEL_DENSITY   0x00002000U /**< window uses high pixel density back buffer if possible */
#define SDL_WINDOW_MOUSE_CAPTURE        0x00004000U /**< window has mouse captured (unrelated to MOUSE_GRABBED) */
#define SDL_WINDOW_ALWAYS_ON_TOP        0x00008000U /**< window should always be above others */
#define SDL_WINDOW_UTILITY              0x00020000U /**< window should be treated as a utility window, not showing in the task bar and window list */
#define SDL_WINDOW_TOOLTIP              0x00040000U /**< window should be treated as a tooltip and does not get mouse or keyboard focus, requires a parent window */
#define SDL_WINDOW_POPUP_MENU           0x00080000U /**< window should be treated as a popup menu, requires a parent window */
#define SDL_WINDOW_KEYBOARD_GRABBED     0x00100000U /**< window has grabbed keyboard input */
#define SDL_WINDOW_VULKAN               0x10000000U /**< window usable for Vulkan surface */
#define SDL_WINDOW_METAL                0x20000000U /**< window usable for Metal view */
#define SDL_WINDOW_TRANSPARENT          0x40000000U /**< window with transparent buffer */
#define SDL_WINDOW_NOT_FOCUSABLE        0x80000000U /**< window should not be focusable */
```

## Remarks

These cover a lot of true/false, or on/off, window state. Some of it is
immutable after being set through [SDL_CreateWindow](SDL_CreateWindow)(),
some of it can be changed on existing windows by the app, and some of it
might be altered by the user or system outside of the app's control.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

