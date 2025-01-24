# SDL_CommonEvent

Fields shared by every event

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_CommonEvent
{
    Uint32 type;
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
} SDL_CommonEvent;
```

## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

