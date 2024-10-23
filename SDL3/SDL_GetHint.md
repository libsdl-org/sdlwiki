###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetHint

Get the value of a hint.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
const char* SDL_GetHint(const char *name);
```

## Function Parameters

|              |          |                    |
| ------------ | -------- | ------------------ |
| const char * | **name** | the hint to query. |

## Return Value

(const char *) Returns the string value of a hint or NULL if the hint isn't
set.

## Thread Safety

It is safe to call this function from any thread, however the return value
only remains valid until the hint is changed; if another thread might do
so, the app should supply locks and/or make a copy of the string. Note that
using a hint callback instead is always thread-safe, as SDL holds a lock on
the thread subsystem during the callback.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetHint](SDL_SetHint)
- [SDL_SetHintWithPriority](SDL_SetHintWithPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)

