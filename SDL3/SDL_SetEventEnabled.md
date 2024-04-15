###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetEventEnabled

Set the state of processing events by type.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_SetEventEnabled(Uint32 type, SDL_bool enabled);

```

## Function Parameters

|                 |                                                                   |
| --------------- | ----------------------------------------------------------------- |
| **type**        | the type of event; see [SDL_EventType](SDL_EventType) for details |
| **enabled**     | whether to process the event or not                               |

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_EventEnabled](SDL_EventEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

