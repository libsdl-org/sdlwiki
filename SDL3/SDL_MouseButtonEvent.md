# SDL_MouseButtonEvent

Mouse button event structure (event.button.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_MouseButtonEvent
{
    SDL_EventType type; /**< SDL_EVENT_MOUSE_BUTTON_DOWN or SDL_EVENT_MOUSE_BUTTON_UP */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID; /**< The window with mouse focus, if any */
    SDL_MouseID which;  /**< The mouse instance id in relative mode, SDL_TOUCH_MOUSEID for touch events, or 0 */
    Uint8 button;       /**< The mouse button index */
    bool down;          /**< true if the button is pressed */
    Uint8 clicks;       /**< 1 for single-click, 2 for double-click, etc. */
    Uint8 padding;
    float x;            /**< X coordinate, relative to window */
    float y;            /**< Y coordinate, relative to window */
} SDL_MouseButtonEvent;
```

## Version

This struct is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

