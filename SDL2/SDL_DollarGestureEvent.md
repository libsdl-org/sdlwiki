###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DollarGestureEvent

Dollar Gesture Event (event.dgesture.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_DollarGestureEvent
{
    Uint32 type;        /**< SDL_DOLLARGESTURE or SDL_DOLLARRECORD */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_TouchID touchId; /**< The touch device id */
    SDL_GestureID gestureId;
    Uint32 numFingers;
    float error;
    float x;            /**< Normalized center of gesture */
    float y;            /**< Normalized center of gesture */
} SDL_DollarGestureEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


