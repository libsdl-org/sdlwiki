###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CommonEvent

Fields shared by every event

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
typedef struct SDL_CommonEvent
{
    Uint32 type;
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
} SDL_CommonEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

