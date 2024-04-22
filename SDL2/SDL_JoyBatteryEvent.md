###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoyBatteryEvent

Joysick battery level change event structure (event.jbattery.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyBatteryEvent
{
    Uint32 type;        /**< ::SDL_JOYBATTERYUPDATED */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    SDL_JoystickPowerLevel level; /**< The joystick battery level */
} SDL_JoyBatteryEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

