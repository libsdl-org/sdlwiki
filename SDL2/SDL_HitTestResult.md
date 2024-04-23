###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HitTestResult

Possible return values from the [SDL_HitTest](SDL_HitTest) callback.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
typedef enum SDL_HitTestResult
{
    SDL_HITTEST_NORMAL,  /**< Region is normal. No special properties. */
    SDL_HITTEST_DRAGGABLE,  /**< Region can drag entire window. */
    SDL_HITTEST_RESIZE_TOPLEFT,
    SDL_HITTEST_RESIZE_TOP,
    SDL_HITTEST_RESIZE_TOPRIGHT,
    SDL_HITTEST_RESIZE_RIGHT,
    SDL_HITTEST_RESIZE_BOTTOMRIGHT,
    SDL_HITTEST_RESIZE_BOTTOM,
    SDL_HITTEST_RESIZE_BOTTOMLEFT,
    SDL_HITTEST_RESIZE_LEFT
} SDL_HitTestResult;
```

## See Also

* [SDL_HitTest](SDL_HitTest)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryEnum](CategoryEnum), [CategoryVideo](CategoryVideo)


