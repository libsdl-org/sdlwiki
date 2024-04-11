###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DisplayEvent

Display state change event data (event.display.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
typedef struct SDL_DisplayEvent
{
    Uint32 type;        /**< ::SDL_DISPLAYEVENT */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 display;     /**< The associated display index */
    Uint8 event;        /**< ::SDL_DisplayEventID */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint32 data1;       /**< event dependent data */
} SDL_DisplayEvent;
```

## Code Examples

```c++
SDL_Event ev;
    
while (SDL_PollEvent(&ev) != 0) {
    if (ev.type == SDL_DISPLAYEVENT) {
        switch (ev.display.event) {
            case SDL_DISPLAYEVENT_CONNECTED:
                SDL_Log("A new display with id %d was connected", ev.display.display);
                break;
            case SDL_DISPLAYEVENT_DISCONNECTED:
                SDL_Log("The display with id %d was disconnected", ev.display.display);
                break;
            case SDL_DISPLAYEVENT_ORIENTATION:
                SDL_Log("The orientation of display with id %d was changed", ev.display.display);
                break;
        }
    }
}
```

## Data Fields

|        |           |                             |
|--------|-----------|-----------------------------|
| Uint32 | **type**      | SDL_DISPLAYEVENT            |
| Uint32 | **timestamp** | Timestamp in milliseconds   |
| Uint32 | **display**   | The associated display index|
| Uint8  | **event**     | [SDL_DisplayEventID](https://wiki.libsdl.org/SDL_DisplayEventID) |
| Sint32 | **data1** | Event associated data|

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

