###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HintCallback

A callback used to send notifications of hint value changes.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
typedef void(SDLCALL *SDL_HintCallback)(void *userdata, const char *name, const char *oldValue, const char *newValue);
```

## Function Parameters

|              |                                                                                |
| ------------ | ------------------------------------------------------------------------------ |
| **userdata** | what was passed as `userdata` to [SDL_AddHintCallback](SDL_AddHintCallback)(). |
| **name**     | what was passed as `name` to [SDL_AddHintCallback](SDL_AddHintCallback)().     |
| **oldValue** | the previous hint value.                                                       |
| **newValue** | the new value hint is to be set to.                                            |

## Remarks

This is called an initial time during
[SDL_AddHintCallback](SDL_AddHintCallback) with the hint's current value,
and then again each time the hint's value changes.

## Thread Safety

This callback is fired from whatever thread is setting a new hint value.
SDL holds a lock on the hint subsystem when calling this callback.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_AddHintCallback](SDL_AddHintCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryHints](CategoryHints)

