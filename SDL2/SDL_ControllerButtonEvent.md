###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ControllerButtonEvent

Game controller button event structure (event.cbutton.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_ControllerButtonEvent
{
    Uint32 type;        /**< SDL_CONTROLLERBUTTONDOWN or SDL_CONTROLLERBUTTONUP */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    Uint8 button;       /**< The controller button (SDL_GameControllerButton) */
    Uint8 state;        /**< SDL_PRESSED or SDL_RELEASED */
    Uint8 padding1;
    Uint8 padding2;
} SDL_ControllerButtonEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents), [CategoryAPIStruct](CategoryAPIStruct), 

