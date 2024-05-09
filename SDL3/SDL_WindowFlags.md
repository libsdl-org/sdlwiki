###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WindowFlags

The flags on a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef Uint64 SDL_WindowFlags;

#define SDL_WINDOW_FULLSCREEN           SDL_UINT64_C(0x0000000000000001)    /**< window is in fullscreen mode */
#define SDL_WINDOW_OPENGL               SDL_UINT64_C(0x0000000000000002)    /**< window usable with OpenGL context */
#define SDL_WINDOW_OCCLUDED             SDL_UINT64_C(0x0000000000000004)    /**< window is occluded */
#define SDL_WINDOW_HIDDEN               SDL_UINT64_C(0x0000000000000008)    /**< window is neither mapped onto the desktop nor shown in the taskbar/dock/window list; SDL_ShowWindow() is required for it to become visible */
#define SDL_WINDOW_BORDERLESS           SDL_UINT64_C(0x0000000000000010)    /**< no window decoration */
#define SDL_WINDOW_RESIZABLE            SDL_UINT64_C(0x0000000000000020)    /**< window can be resized */
#define SDL_WINDOW_MINIMIZED            SDL_UINT64_C(0x0000000000000040)    /**< window is minimized */
#define SDL_WINDOW_MAXIMIZED            SDL_UINT64_C(0x0000000000000080)    /**< window is maximized */
#define SDL_WINDOW_MOUSE_GRABBED        SDL_UINT64_C(0x0000000000000100)    /**< window has grabbed mouse input */
#define SDL_WINDOW_INPUT_FOCUS          SDL_UINT64_C(0x0000000000000200)    /**< window has input focus */
#define SDL_WINDOW_MOUSE_FOCUS          SDL_UINT64_C(0x0000000000000400)    /**< window has mouse focus */
#define SDL_WINDOW_EXTERNAL             SDL_UINT64_C(0x0000000000000800)    /**< window not created by SDL */
#define SDL_WINDOW_MODAL                SDL_UINT64_C(0x0000000000001000)    /**< window is modal */
#define SDL_WINDOW_HIGH_PIXEL_DENSITY   SDL_UINT64_C(0x0000000000002000)    /**< window uses high pixel density back buffer if possible */
#define SDL_WINDOW_MOUSE_CAPTURE        SDL_UINT64_C(0x0000000000004000)    /**< window has mouse captured (unrelated to MOUSE_GRABBED) */
#define SDL_WINDOW_ALWAYS_ON_TOP        SDL_UINT64_C(0x0000000000008000)    /**< window should always be above others */
#define SDL_WINDOW_UTILITY              SDL_UINT64_C(0x0000000000020000)    /**< window should be treated as a utility window, not showing in the task bar and window list */
#define SDL_WINDOW_TOOLTIP              SDL_UINT64_C(0x0000000000040000)    /**< window should be treated as a tooltip and does not get mouse or keyboard focus, requires a parent window */
#define SDL_WINDOW_POPUP_MENU           SDL_UINT64_C(0x0000000000080000)    /**< window should be treated as a popup menu, requires a parent window */
#define SDL_WINDOW_KEYBOARD_GRABBED     SDL_UINT64_C(0x0000000000100000)    /**< window has grabbed keyboard input */
#define SDL_WINDOW_VULKAN               SDL_UINT64_C(0x0000000010000000)    /**< window usable for Vulkan surface */
#define SDL_WINDOW_METAL                SDL_UINT64_C(0x0000000020000000)    /**< window usable for Metal view */
#define SDL_WINDOW_TRANSPARENT          SDL_UINT64_C(0x0000000040000000)    /**< window with transparent buffer */
#define SDL_WINDOW_NOT_FOCUSABLE        SDL_UINT64_C(0x0000000080000000)    /**< window should not be focusable */
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

