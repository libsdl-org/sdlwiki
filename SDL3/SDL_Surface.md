###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Surface

A collection of pixels used in software blitting.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef struct SDL_Surface
{
    Uint32 flags;               /**< Read-only */
    SDL_PixelFormat *format;    /**< Read-only */
    int w, h;                   /**< Read-only */
    int pitch;                  /**< Read-only */
    void *pixels;               /**< Read-write */

    void *reserved;             /**< Private */

    /** information needed for surfaces requiring locks */
    int locked;                 /**< Read-only */

    /** list of BlitMap that hold a reference to this surface */
    void *list_blitmap;         /**< Private */

    /** clipping information */
    SDL_Rect clip_rect;         /**< Read-only */

    /** info for fast blit mapping to other surfaces */
    SDL_BlitMap *map;           /**< Private */

    /** Reference count -- used when freeing surface */
    int refcount;               /**< Read-mostly */
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

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

