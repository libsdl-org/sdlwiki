###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SurfaceFlags

The flags on an [SDL_Surface](SDL_Surface).

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
typedef Uint32 SDL_SurfaceFlags;

#define SDL_SWSURFACE               0           /**< Just here for compatibility */
#define SDL_PREALLOC                0x00000001  /**< Surface uses preallocated memory */
#define SDL_RLEACCEL                0x00000002  /**< Surface is RLE encoded */
#define SDL_DONTFREE                0x00000004  /**< Surface is referenced internally */
#define SDL_SIMD_ALIGNED            0x00000008  /**< Surface uses aligned memory */
#define SDL_SURFACE_USES_PROPERTIES 0x00000010  /**< Surface uses properties */
```

## Remarks

These are generally meant to be considered read-only.

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySurface](CategorySurface)

