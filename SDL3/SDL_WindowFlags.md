###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WindowFlags

The flags on a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef Uint32 SDL_WindowFlags;

#define SDL_WINDOW_FULLSCREEN           0x00000001u /**< window is in fullscreen mode */
#define SDL_WINDOW_OPENGL               0x00000002u /**< window usable with OpenGL context */
#define SDL_WINDOW_OCCLUDED             0x00000004u /**< window is occluded */
#define SDL_WINDOW_HIDDEN               0x00000008u /**< window is neither mapped onto the desktop nor shown in the taskbar/dock/window list; SDL_ShowWindow() is required for it to become visible */
#define SDL_WINDOW_BORDERLESS           0x00000010u /**< no window decoration */
#define SDL_WINDOW_RESIZABLE            0x00000020u /**< window can be resized */
#define SDL_WINDOW_MINIMIZED            0x00000040u /**< window is minimized */
#define SDL_WINDOW_MAXIMIZED            0x00000080u /**< window is maximized */
#define SDL_WINDOW_MOUSE_GRABBED        0x00000100u /**< window has grabbed mouse input */
#define SDL_WINDOW_INPUT_FOCUS          0x00000200u /**< window has input focus */
#define SDL_WINDOW_MOUSE_FOCUS          0x00000400u /**< window has mouse focus */
#define SDL_WINDOW_EXTERNAL             0x00000800u /**< window not created by SDL */
#define SDL_WINDOW_MODAL                0x00001000u /**< window is modal */
#define SDL_WINDOW_HIGH_PIXEL_DENSITY   0x00002000u /**< window uses high pixel density back buffer if possible */
#define SDL_WINDOW_MOUSE_CAPTURE        0x00004000u /**< window has mouse captured (unrelated to MOUSE_GRABBED) */
#define SDL_WINDOW_ALWAYS_ON_TOP        0x00008000u /**< window should always be above others */
#define SDL_WINDOW_UTILITY              0x00020000u /**< window should be treated as a utility window, not showing in the task bar and window list */
#define SDL_WINDOW_TOOLTIP              0x00040000u /**< window should be treated as a tooltip and does not get mouse or keyboard focus, requires a parent window */
#define SDL_WINDOW_POPUP_MENU           0x00080000u /**< window should be treated as a popup menu, requires a parent window */
#define SDL_WINDOW_KEYBOARD_GRABBED     0x00100000u /**< window has grabbed keyboard input */
#define SDL_WINDOW_VULKAN               0x10000000u /**< window usable for Vulkan surface */
#define SDL_WINDOW_METAL                0x20000000u /**< window usable for Metal view */
#define SDL_WINDOW_TRANSPARENT          0x40000000u /**< window with transparent buffer */
#define SDL_WINDOW_NOT_FOCUSABLE        0x80000000u /**< window should not be focusable */
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

