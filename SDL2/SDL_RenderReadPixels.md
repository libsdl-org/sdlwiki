###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderReadPixels

Read pixels from the current rendering target to an array of pixels.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderReadPixels(SDL_Renderer * renderer,
                     const SDL_Rect * rect,
                     Uint32 format,
                     void *pixels, int pitch);
```

## Function Parameters

|                                |              |                                                                                                                                              |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                                       |
| const [SDL_Rect](SDL_Rect) *   | **rect**     | an [SDL_Rect](SDL_Rect) structure representing the area to read, or NULL for the entire render target.                                       |
| Uint32                         | **format**   | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum) value of the desired format of the pixel data, or 0 to use the format of the rendering target. |
| void *                         | **pixels**   | a pointer to the pixel data to copy into.                                                                                                    |
| int                            | **pitch**    | the pitch of the `pixels` parameter.                                                                                                         |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

**WARNING**: This is a very slow operation, and should not be used
frequently. If you're using this on the main rendering target, it should be
called after rendering and before [SDL_RenderPresent](SDL_RenderPresent)().

`pitch` specifies the number of bytes between rows in the destination
`pixels` data. This allows you to write to a subrectangle or have padded
rows in the destination. Generally, `pitch` should equal the number of
pixels per row in the `pixels` data times the number of bytes per pixel,
but it might contain additional padding (for example, 24bit RGB Windows
Bitmap data pads all rows to multiples of 4 bytes).

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

