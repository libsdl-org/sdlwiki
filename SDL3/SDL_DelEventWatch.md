###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DelEventWatch

Remove an event watch callback added with [SDL_AddEventWatch](SDL_AddEventWatch.md)().

## Syntax

```c
void SDL_DelEventWatch(SDL_EventFilter filter, void *userdata);

```

## Function Parameters

|                  |                                                                            |
| ---------------- | -------------------------------------------------------------------------- |
| **filter**       | the function originally passed to [SDL_AddEventWatch](SDL_AddEventWatch.md)() |
| **userdata**     | the pointer originally passed to [SDL_AddEventWatch](SDL_AddEventWatch.md)()  |

## Remarks

This function takes the same input as
[SDL_AddEventWatch](SDL_AddEventWatch.md)() to identify and delete the
corresponding callback.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AddEventWatch](SDL_AddEventWatch.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryEvents](CategoryEvents.md)
