# SDL_AddHintCallback

Add a function to watch a particular hint.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
void SDL_AddHintCallback(const char *name,
                         SDL_HintCallback callback,
                         void *userdata);
```

## Function Parameters

|                                      |              |                                                                                                   |
| ------------------------------------ | ------------ | ------------------------------------------------------------------------------------------------- |
| const char *                         | **name**     | the hint to watch.                                                                                |
| [SDL_HintCallback](SDL_HintCallback) | **callback** | An [SDL_HintCallback](SDL_HintCallback) function that will be called when the hint value changes. |
| void *                               | **userdata** | a pointer to pass to the callback function.                                                       |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_DelHintCallback](SDL_DelHintCallback)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)

