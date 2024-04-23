###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SysWMmsg

The custom event structure.

## Header File

Defined in [SDL_syswm.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_syswm.h)

## Syntax

```c
struct SDL_SysWMmsg
{
    SDL_version version;
    SDL_SYSWM_TYPE subsystem;
    union
    {
#if defined(SDL_VIDEO_DRIVER_WINDOWS)
        struct {
            HWND hwnd;                  /**< The window for the message */
            UINT msg;                   /**< The type of message */
            WPARAM wParam;              /**< WORD message parameter */
            LPARAM lParam;              /**< LONG message parameter */
        } win;
#endif
#if defined(SDL_VIDEO_DRIVER_X11)
        struct {
            XEvent event;
        } x11;
#endif
#if defined(SDL_VIDEO_DRIVER_DIRECTFB)
        struct {
            DFBEvent event;
        } dfb;
#endif
#if defined(SDL_VIDEO_DRIVER_COCOA)
        struct
        {
            /* Latest version of Xcode clang complains about empty structs in C v. C++:
                 error: empty struct has size 0 in C, size 1 in C++
             */
            int dummy;
            /* No Cocoa window events yet */
        } cocoa;
#endif
#if defined(SDL_VIDEO_DRIVER_UIKIT)
        struct
        {
            int dummy;
            /* No UIKit window events yet */
        } uikit;
#endif
#if defined(SDL_VIDEO_DRIVER_VIVANTE)
        struct
        {
            int dummy;
            /* No Vivante window events yet */
        } vivante;
#endif
#if defined(SDL_VIDEO_DRIVER_OS2)
        struct
        {
            BOOL fFrame;                /**< TRUE if hwnd is a frame window */
            HWND hwnd;                  /**< The window receiving the message */
            ULONG msg;                  /**< The message identifier */
            MPARAM mp1;                 /**< The first first message parameter */
            MPARAM mp2;                 /**< The second first message parameter */
        } os2;
#endif
        /* Can't have an empty union */
        int dummy;
    } msg;
};
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategorySWM](CategorySWM)


