###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MouseMotionEvent

Mouse motion event structure (event.motion.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_MouseMotionEvent
{
    Uint32 type;        /**< ::SDL_MOUSEMOTION */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 windowID;    /**< The window with mouse focus, if any */
    Uint32 which;       /**< The mouse instance id, or SDL_TOUCH_MOUSEID */
    Uint32 state;       /**< The current button state */
    Sint32 x;           /**< X coordinate, relative to window */
    Sint32 y;           /**< Y coordinate, relative to window */
    Sint32 xrel;        /**< The relative motion in the X direction */
    Sint32 yrel;        /**< The relative motion in the Y direction */
} SDL_MouseMotionEvent;
```

## Data Fields

|        |               |                                                                      |
| ------ | ------------- | -------------------------------------------------------------------- |
| Uint32 | **type**      | the event type; SDL_MOUSEMOTION                                      |
| Uint32 | **timestamp** | timestamp of the event                                               |
| Uint32 | **windowID**  | the window with mouse focus, if any                                  |
| Uint32 | **which**     | the mouse instance id, or SDL_TOUCH_MOUSEID; see Remarks for details |
| Uint32 | **state**     | the state of the button; see Remarks for details                     |
| Sint32 | **x**         | X coordinate, relative to window                                     |
| Sint32 | **y**         | Y coordinate, relative to window                                     |
| Sint32 | **xrel**      | relative motion in the X direction                                   |
| Sint32 | **yrel**      | relative motion in the Y direction                                   |

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)
[SDL_MouseButtonEvent](SDL_MouseButtonEvent)
[SDL_MouseWheelEvent](SDL_MouseWheelEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


