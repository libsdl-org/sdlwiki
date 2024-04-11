###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_YUV_CONVERSION_MODE

The formula used for converting between YUV and RGB

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
typedef enum SDL_YUV_CONVERSION_MODE
{
    SDL_YUV_CONVERSION_JPEG,        /**< Full range JPEG */
    SDL_YUV_CONVERSION_BT601,       /**< BT.601 (the default) */
    SDL_YUV_CONVERSION_BT709,       /**< BT.709 */
    SDL_YUV_CONVERSION_AUTOMATIC    /**< BT.601 for SD content, BT.709 for HD content */
} SDL_YUV_CONVERSION_MODE;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

