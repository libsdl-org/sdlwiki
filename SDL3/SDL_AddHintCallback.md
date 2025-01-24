# SDL_AddHintCallback

Add a function to watch a particular hint.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
bool SDL_AddHintCallback(const char *name, SDL_HintCallback callback, void *userdata);
```

## Function Parameters

|                                      |              |                                                                                                   |
| ------------------------------------ | ------------ | ------------------------------------------------------------------------------------------------- |
| const char *                         | **name**     | the hint to watch.                                                                                |
| [SDL_HintCallback](SDL_HintCallback) | **callback** | An [SDL_HintCallback](SDL_HintCallback) function that will be called when the hint value changes. |
| void *                               | **userdata** | a pointer to pass to the callback function.                                                       |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The callback function is called _during_ this function, to provide it an
initial value, and again each time the hint's value changes.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RemoveHintCallback](SDL_RemoveHintCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)

