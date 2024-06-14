###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DelEventWatch

Remove an event watch callback added with [SDL_AddEventWatch](SDL_AddEventWatch)().

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
void SDL_DelEventWatch(SDL_EventFilter filter,
                   void *userdata);
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

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

