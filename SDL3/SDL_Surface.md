###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Surface

A collection of pixels used in software blitting.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
typedef struct SDL_Surface
{
    SDL_SurfaceFlags flags;     /**< Read-only */
    SDL_PixelFormat format;     /**< Read-only */
    int w, h;                   /**< Read-only */
    int pitch;                  /**< Read-only */
    void *pixels;               /**< Read-only pointer, writable pixels if non-NULL */

    int refcount;               /**< Application reference count, used when freeing surface */

    SDL_SurfaceData *internal;  /**< Private */

} SDL_Surface;
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

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategorySurface](CategorySurface)

