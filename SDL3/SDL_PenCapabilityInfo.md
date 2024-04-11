###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PenCapabilityInfo

Pen capabilities, as reported by [SDL_GetPenCapabilities](SDL_GetPenCapabilities)()

## Header File

Defined in [SDL_pen.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef struct SDL_PenCapabilityInfo
{
    float max_tilt;    /**< Physical maximum tilt angle, for XTILT and YTILT, or SDL_PEN_INFO_UNKNOWN .  Pens cannot typically tilt all the way to 90 degrees, so this value is usually less than 90.0. */
    Uint32 wacom_id;   /**< For Wacom devices: wacom tool type ID, otherwise 0 (useful e.g. with libwacom) */
    Sint8 num_buttons; /**< Number of pen buttons (not counting the pen tip), or SDL_PEN_INFO_UNKNOWN */
} SDL_PenCapabilityInfo;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

