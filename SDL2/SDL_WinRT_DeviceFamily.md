###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WinRT_DeviceFamily

WinRT Device Family

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
typedef enum SDL_WinRT_DeviceFamily
{
    /** \brief Unknown family  */
    SDL_WINRT_DEVICEFAMILY_UNKNOWN,

    /** \brief Desktop family*/
    SDL_WINRT_DEVICEFAMILY_DESKTOP,

    /** \brief Mobile family (for example smartphone) */
    SDL_WINRT_DEVICEFAMILY_MOBILE,

    /** \brief XBox family */
    SDL_WINRT_DEVICEFAMILY_XBOX,
} SDL_WinRT_DeviceFamily;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

