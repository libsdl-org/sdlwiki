###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetHint

Set a hint with normal priority.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
bool SDL_SetHint(const char *name, const char *value);
```

## Function Parameters

|              |           |                                 |
| ------------ | --------- | ------------------------------- |
| const char * | **name**  | the hint to set.                |
| const char * | **value** | the value of the hint variable. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Hints will not be set if there is an existing override hint or environment
variable that takes precedence. You can use
[SDL_SetHintWithPriority](SDL_SetHintWithPriority)() to set the hint with
override priority instead.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetHint](SDL_GetHint)
- [SDL_ResetHint](SDL_ResetHint)
- [SDL_SetHintWithPriority](SDL_SetHintWithPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)

