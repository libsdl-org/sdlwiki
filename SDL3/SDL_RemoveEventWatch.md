# SDL_RemoveEventWatch

Remove an event watch callback added with [SDL_AddEventWatch](SDL_AddEventWatch)().

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void SDL_RemoveEventWatch(SDL_EventFilter filter, void *userdata);
```

## Function Parameters

|                                    |              |                                                                             |
| ---------------------------------- | ------------ | --------------------------------------------------------------------------- |
| [SDL_EventFilter](SDL_EventFilter) | **filter**   | the function originally passed to [SDL_AddEventWatch](SDL_AddEventWatch)(). |
| void *                             | **userdata** | the pointer originally passed to [SDL_AddEventWatch](SDL_AddEventWatch)().  |

## Remarks

This function takes the same input as
[SDL_AddEventWatch](SDL_AddEventWatch)() to identify and delete the
corresponding callback.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

