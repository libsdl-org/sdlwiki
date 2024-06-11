###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AddHintCallback

Add a function to watch a particular hint.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
int SDL_AddHintCallback(const char *name,
                    SDL_HintCallback callback,
                    void *userdata);
```

## Function Parameters

|                  |                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| **name**         | the hint to watch                                                                                |
| **callback**     | An [SDL_HintCallback](SDL_HintCallback) function that will be called when the hint value changes |
| **userdata**     | a pointer to pass to the callback function                                                       |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is **NOT** safe to call this function from two threads at once.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_DelHintCallback](SDL_DelHintCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)

