###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Surface

A collection of pixels used in software blitting.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
typedef struct SDL_Surface
{
    Uint32 flags;               /**< Read-only */
    SDL_PixelFormat *format;    /**< Read-only */
    int w, h;                   /**< Read-only */
    int pitch;                  /**< Read-only */
    void *pixels;               /**< Read-write */

    /** Application data associated with the surface */
    void *userdata;             /**< Read-write */

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

## Code Examples

```c
/* This is meant to show how to edit a surface's pixels on the CPU, but
   normally you should use SDL_FillRect() to wipe a surface's contents. */
void WipeSurface(SDL_Surface *surface)
{
    /* This is fast for surfaces that don't require locking. */
    /* Once locked, surface->pixels is safe to access. */
    SDL_LockSurface(surface);

    /* This assumes that color value zero is black. Use
       SDL_MapRGBA() for more robust surface color mapping! */
    /* height times pitch is the size of the surface's whole buffer. */
    SDL_memset(surface->pixels, 0, surface->h * surface->pitch);

    SDL_UnlockSurface(surface);
}
```

## Data Fields

|                                                              |                                                                 |                                                                                                                                           |
| ------------------------------------------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| <span style="color: rgb(128, 128, 128);">Uint32</span>       | <span style="color: rgb(128, 128, 128);">'''flags'''</span>     | <span style="color: rgb(128, 128, 128);">(internal use)</span>                                                                            |
| [SDL_PixelFormat](SDL_PixelFormat)*                          | '''format'''                                                    | the format of the pixels stored in the surface; see [SDL_PixelFormat](SDL_PixelFormat) for details (read-only)                            |
| int                                                          | '''w, h'''                                                      | the width and height in pixels (read-only)                                                                                                |
| int                                                          | '''pitch'''                                                     | the length of a row of pixels in bytes (read-only)                                                                                        |
| void*                                                        | '''pixels'''                                                    | the pointer to the actual pixel data; see Remarks for details (read-write)                                                                |
| void*                                                        | '''userdata'''                                                  | an arbitrary pointer you can set (read-write)                                                                                             |
| <span style="color: rgb(128, 128, 128);">int</span>          | <span style="color: rgb(128, 128, 128);">'''locked'''</span>    | <span style="color: rgb(128, 128, 128);">used for surfaces that require locking (internal use)</span>                                     |
| <span style="color: rgb(128, 128, 128);">void*</span>        | <span style="color: rgb(128, 128, 128);">'''lock_data'''</span> | <span style="color: rgb(128, 128, 128);">used for surfaces that require locking (internal use)</span>                                     |
| [SDL_Rect](SDL_Rect)                                         | '''clip_rect'''                                                 | an [SDL_Rect](SDL_Rect) structure used to clip blits to the surface which can be set by [SDL_SetClipRect](SDL_SetClipRect)() (read-only)  |
| <span style="color: rgb(128, 128, 128);">SDL_BlitMap*</span> | <span style="color: rgb(128, 128, 128);">'''map'''</span>       | <span style="color: rgb(128, 128, 128);">info for fast blit mapping to other surfaces (internal use)</span>                               |
| int                                                          | '''refcount'''                                                  | reference count that can be incremented by the application                                                                                |

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategorySurface](CategorySurface)


