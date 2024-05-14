###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DisplayEventID

Event subtype for display events

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
typedef enum SDL_DisplayEventID
{
    SDL_DISPLAYEVENT_NONE,          /**< Never used */
    SDL_DISPLAYEVENT_ORIENTATION,   /**< Display orientation has changed to data1 */
    SDL_DISPLAYEVENT_CONNECTED,     /**< Display has been added to the system */
    SDL_DISPLAYEVENT_DISCONNECTED,  /**< Display has been removed from the system */
    SDL_DISPLAYEVENT_MOVED          /**< Display has changed position */
} SDL_DisplayEventID;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryVideo](CategoryVideo), [CategoryAPIEnum](CategoryAPIEnum), [CategoryEvents](CategoryEvents)


