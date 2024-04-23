###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SYSWM_TYPE

These are the various supported windowing subsystems

## Header File

Defined in [SDL_syswm.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_syswm.h)

## Syntax

```c
typedef enum SDL_SYSWM_TYPE
{
    SDL_SYSWM_UNKNOWN,
    SDL_SYSWM_WINDOWS,
    SDL_SYSWM_X11,
    SDL_SYSWM_DIRECTFB,
    SDL_SYSWM_COCOA,
    SDL_SYSWM_UIKIT,
    SDL_SYSWM_WAYLAND,
    SDL_SYSWM_MIR,  /* no longer available, left for API/ABI compatibility. Remove in 2.1! */
    SDL_SYSWM_WINRT,
    SDL_SYSWM_ANDROID,
    SDL_SYSWM_VIVANTE,
    SDL_SYSWM_OS2,
    SDL_SYSWM_HAIKU,
    SDL_SYSWM_KMSDRM,
    SDL_SYSWM_RISCOS
} SDL_SYSWM_TYPE;
```

## Related Structures

[SDL_SysWMinfo](SDL_SysWMinfo)
[SDL_SysWMmsg](SDL_SysWMmsg)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryEnum](CategoryEnum), [CategorySWM](CategorySWM)


