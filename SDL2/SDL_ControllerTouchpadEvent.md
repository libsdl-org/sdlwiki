###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ControllerTouchpadEvent

Game controller touchpad event structure (event.ctouchpad.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_ControllerTouchpadEvent
{
    Uint32 type;        /**< SDL_CONTROLLERTOUCHPADDOWN or SDL_CONTROLLERTOUCHPADMOTION or SDL_CONTROLLERTOUCHPADUP */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    Sint32 touchpad;    /**< The index of the touchpad */
    Sint32 finger;      /**< The index of the finger on the touchpad */
    float x;            /**< Normalized in the range 0...1 with 0 being on the left */
    float y;            /**< Normalized in the range 0...1 with 0 being at the top */
    float pressure;     /**< Normalized in the range 0...1 */
} SDL_ControllerTouchpadEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

