###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_KeyboardEvent

Keyboard button event structure (event.key.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_KeyboardEvent
{
    SDL_EventType type;     /**< SDL_EVENT_KEY_DOWN or SDL_EVENT_KEY_UP */
    Uint32 reserved;
    Uint64 timestamp;       /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID;  /**< The window with keyboard focus, if any */
    SDL_KeyboardID which;   /**< The keyboard instance id, or 0 if unknown or virtual */
    SDL_Scancode scancode;  /**< SDL physical key code */
    SDL_Keycode key;        /**< SDL virtual key code */
    SDL_Keymod mod;         /**< current key modifiers */
    Uint16 raw;             /**< The platform dependent scancode for this event */
    Uint8 state;            /**< SDL_PRESSED or SDL_RELEASED */
    Uint8 repeat;           /**< Non-zero if this is a key repeat */
} SDL_KeyboardEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

