# SDL_TouchFingerEvent

Touch finger event structure (event.tfinger.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_TouchFingerEvent
{
    SDL_EventType type; /**< SDL_EVENT_FINGER_DOWN, SDL_EVENT_FINGER_UP, SDL_EVENT_FINGER_MOTION, or SDL_EVENT_FINGER_CANCELED */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_TouchID touchID; /**< The touch device id */
    SDL_FingerID fingerID;
    float x;            /**< Normalized in the range 0...1 */
    float y;            /**< Normalized in the range 0...1 */
    float dx;           /**< Normalized in the range -1...1 */
    float dy;           /**< Normalized in the range -1...1 */
    float pressure;     /**< Normalized in the range 0...1 */
    SDL_WindowID windowID; /**< The window underneath the finger, if any */
} SDL_TouchFingerEvent;
```

## Remarks

Coordinates in this event are normalized. `x` and `y` are normalized to a
range between 0.0f and 1.0f, relative to the window, so (0,0) is the top
left and (1,1) is the bottom right. Delta coordinates `dx` and `dy` are
normalized in the ranges of -1.0f (traversed all the way from the bottom or
right to all the way up or left) to 1.0f (traversed all the way from the
top or left to all the way down or right).

Note that while the coordinates are _normalized_, they are not _clamped_,
which means in some circumstances you can get a value outside of this
range. For example, a renderer using logical presentation might give a
negative value when the touch is in the letterboxing. Some platforms might
report a touch outside of the window, which will also be outside of the
range.

## Version

This struct is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

