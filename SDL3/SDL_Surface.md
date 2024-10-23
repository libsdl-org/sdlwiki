###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_Surface

A collection of pixels used in software blitting.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
struct SDL_Surface
{
    SDL_SurfaceFlags flags;     /**< The flags of the surface, read-only */
    SDL_PixelFormat format;     /**< The format of the surface, read-only */
    int w;                      /**< The width of the surface, read-only. */
    int h;                      /**< The height of the surface, read-only. */
    int pitch;                  /**< The distance in bytes between rows of pixels, read-only */
    void *pixels;               /**< A pointer to the pixels of the surface, the pixels are writeable if non-NULL */

    int refcount;               /**< Application reference count, used when freeing surface */

    void *reserved;             /**< Reserved for internal use */
};
```

## Remarks

Pixels are arranged in memory in rows, with the top row first. Each row
occupies an amount of memory given by the pitch (sometimes known as the row
stride in non-SDL APIs).

Within each row, pixels are arranged from left to right until the width is
reached. Each pixel occupies a number of bits appropriate for its format,
with most formats representing each pixel as one or more whole bytes (in
some indexed formats, instead multiple pixels are packed into each byte),
and a byte order given by the format. After encoding all pixels, any
remaining bytes to reach the pitch are used as padding to reach a desired
alignment, and have undefined contents.

## Version

This struct is available since SDL 3.1.3.

## See Also

- [SDL_CreateSurface](SDL_CreateSurface)
- [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategorySurface](CategorySurface)

