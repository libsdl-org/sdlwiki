###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DisplayMode

The structure that defines a display mode.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef struct SDL_DisplayMode
{
    SDL_DisplayID displayID;    /**< the display this mode is associated with */
    SDL_PixelFormatEnum format; /**< pixel format */
    int w;                      /**< width */
    int h;                      /**< height */
    float pixel_density;        /**< scale converting size to pixels (e.g. a 1920x1080 mode with 2.0 scale would have 3840x2160 pixels) */
    float refresh_rate;         /**< refresh rate (or zero for unspecified) */
    void *driverdata;           /**< driver-specific data, initialize to 0 */
} SDL_DisplayMode;
```

## Version

This struct is available since SDL 3.0.0.

## See Also

* [SDL_GetFullscreenDisplayModes](SDL_GetFullscreenDisplayModes)
* [SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode)
* [SDL_GetCurrentDisplayMode](SDL_GetCurrentDisplayMode)
* [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)
* [SDL_GetWindowFullscreenMode](SDL_GetWindowFullscreenMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

