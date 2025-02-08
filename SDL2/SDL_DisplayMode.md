# SDL_DisplayMode

The structure that defines a display mode

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
typedef struct SDL_DisplayMode
{
    Uint32 format;              /**< pixel format */
    int w;                      /**< width, in screen coordinates */
    int h;                      /**< height, in screen coordinates */
    int refresh_rate;           /**< refresh rate (or zero for unspecified) */
    void *driverdata;           /**< driver-specific data, initialize to 0 */
} SDL_DisplayMode;
```

## See Also

- [SDL_GetNumDisplayModes](SDL_GetNumDisplayModes)
- [SDL_GetDisplayMode](SDL_GetDisplayMode)
- [SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode)
- [SDL_GetCurrentDisplayMode](SDL_GetCurrentDisplayMode)
- [SDL_GetClosestDisplayMode](SDL_GetClosestDisplayMode)
- [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode)
- [SDL_GetWindowDisplayMode](SDL_GetWindowDisplayMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryVideo](CategoryVideo)

