###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DelEventWatch

Remove an event watch callback added with [SDL_AddEventWatch](SDL_AddEventWatch)().

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_DelEventWatch(SDL_EventFilter filter, void *userdata);

```

## Function Parameters

|                  |                                                                            |
| ---------------- | -------------------------------------------------------------------------- |
| **filter**       | the function originally passed to [SDL_AddEventWatch](SDL_AddEventWatch)() |
| **userdata**     | the pointer originally passed to [SDL_AddEventWatch](SDL_AddEventWatch)()  |

## Remarks

This function takes the same input as
[SDL_AddEventWatch](SDL_AddEventWatch)() to identify and delete the
corresponding callback.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryEvents](CategoryEvents)


