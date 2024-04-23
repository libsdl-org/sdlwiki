###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MouseWheelEvent

Mouse wheel event structure (event.wheel.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_MouseWheelEvent
{
    Uint32 type;        /**< ::SDL_MOUSEWHEEL */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 windowID;    /**< The window with mouse focus, if any */
    Uint32 which;       /**< The mouse instance id, or SDL_TOUCH_MOUSEID */
    Sint32 x;           /**< The amount scrolled horizontally, positive to the right and negative to the left */
    Sint32 y;           /**< The amount scrolled vertically, positive away from the user and negative toward the user */
    Uint32 direction;   /**< Set to one of the SDL_MOUSEWHEEL_* defines. When FLIPPED the values in X and Y will be opposite. Multiply by -1 to change them back */
    float preciseX;     /**< The amount scrolled horizontally, positive to the right and negative to the left, with float precision (added in 2.0.18) */
    float preciseY;     /**< The amount scrolled vertically, positive away from the user and negative toward the user, with float precision (added in 2.0.18) */
    Sint32 mouseX;      /**< X coordinate, relative to window (added in 2.26.0) */
    Sint32 mouseY;      /**< Y coordinate, relative to window (added in 2.26.0) */
} SDL_MouseWheelEvent;
```

## Code Examples

```c++

SDL_Event event;
while( SDL_PollEvent( &event ) )
{
    if(event.type == SDL_MOUSEWHEEL)
    {
        if(event.wheel.y > 0) // scroll up
        {
             // Put code for handling "scroll up" here!
        }
        else if(event.wheel.y < 0) // scroll down
        {
             // Put code for handling "scroll down" here!
        }

        if(event.wheel.x > 0) // scroll right
        {
             // ...
        }
        else if(event.wheel.x < 0) // scroll left
        {
             // ...
        }
    }
    else if(event.type == SDL_MOUSEBUTTONDOWN)
    {
        // ... handle mouse clicks ...
    }

    // ... handle other kinds of events ...
}
```

## Data Fields

|        |                 |                                                                                                                                  |
| ------ | --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Uint32 | '''type'''      | SDL_MOUSEWHEEL                                                                                                                   |
| Uint32 | '''timestamp''' | timestamp of the event                                                                                                           |
| Uint32 | '''windowID'''  | the window with mouse focus, if any                                                                                              |
| Uint32 | '''which'''     | the mouse instance id, or SDL_TOUCH_MOUSEID; see Remarks for details                                                             |
| Sint32 | '''x'''         | the amount scrolled horizontally, positive to the right and negative to the left                                                 |
| Sint32 | '''y'''         | the amount scrolled vertically, positive away from the user and negative towards the user                                        |
| Uint32 | '''direction''' | SDL_MOUSEWHEEL_NORMAL or SDL_MOUSEWHEEL_FLIPPED; see Remarks for details (>= SDL 2.0.4)                                          |
| float  | '''preciseX'''  | the amount scrolled horizontally, positive to the right and negative to the left, with float precision (added in 2.0.18)         |
| float  | '''preciseY'''  | the amount scrolled vertically, positive away from the user and negative toward the user, with float precision (added in 2.0.18) |

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)
[SDL_MouseButtonEvent](SDL_MouseButtonEvent)
[SDL_MouseMotionEvent](SDL_MouseMotionEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


