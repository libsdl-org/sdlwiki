###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TouchFingerEvent

Touch finger event structure (event.tfinger.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_TouchFingerEvent
{
    Uint32 type;        /**< ::SDL_FINGERMOTION or ::SDL_FINGERDOWN or ::SDL_FINGERUP */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_TouchID touchId; /**< The touch device id */
    SDL_FingerID fingerId;
    float x;            /**< Normalized in the range 0...1 */
    float y;            /**< Normalized in the range 0...1 */
    float dx;           /**< Normalized in the range -1...1 */
    float dy;           /**< Normalized in the range -1...1 */
    float pressure;     /**< Normalized in the range 0...1 */
    Uint32 windowID;    /**< The window underneath the finger, if any */
} SDL_TouchFingerEvent;
```

## Data Fields

|              |                 |                                                            |
| ------------ | --------------- | ---------------------------------------------------------- |
| Uint32       | '''type'''      | SDL_FINGERMOTION, SDL_FINGERDOWN, or SDL_FINGERUP          |
| Uint32       | '''timestamp''' | timestamp of the event                                     |
| SDL_TouchID  | '''touchId'''   | the touch device id                                        |
| SDL_FingerID | '''fingerId'''  | the finger id                                              |
| float        | '''x'''         | the x-axis location of the touch event, normalized (0...1) |
| float        | '''y'''         | the y-axis location of the touch event, normalized (0...1) |
| float        | '''dx'''        | the distance moved in the x-axis, normalized (-1...1)      |
| float        | '''dy'''        | the distance moved in the y-axis, normalized (-1...1)      |
| float        | '''pressure'''  | the quantity of pressure applied, normalized (0...1)       |
| Uint32       | '''windowID'''  | the window underneath the finger, if any                   |

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


