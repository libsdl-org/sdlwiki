# SDL_MouseWheelEvent

Mouse wheel event structure (event.wheel.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_MouseWheelEvent
{
    SDL_EventType type; /**< SDL_EVENT_MOUSE_WHEEL */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID; /**< The window with mouse focus, if any */
    SDL_MouseID which;  /**< The mouse instance id in relative mode or 0 */
    float x;            /**< The amount scrolled horizontally, positive to the right and negative to the left */
    float y;            /**< The amount scrolled vertically, positive away from the user and negative toward the user */
    SDL_MouseWheelDirection direction; /**< Set to one of the SDL_MOUSEWHEEL_* defines. When FLIPPED the values in X and Y will be opposite. Multiply by -1 to change them back */
    float mouse_x;      /**< X coordinate, relative to window */
    float mouse_y;      /**< Y coordinate, relative to window */
    Sint32 integer_x;   /**< The amount scrolled horizontally, accumulated to whole scroll "ticks" (added in 3.2.12) */
    Sint32 integer_y;   /**< The amount scrolled vertically, accumulated to whole scroll "ticks" (added in 3.2.12) */
} SDL_MouseWheelEvent;
```

## Version

This struct is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

