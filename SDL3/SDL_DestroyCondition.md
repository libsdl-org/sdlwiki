# SDL_DestroyCondition

Destroy a condition variable.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_DestroyCondition(SDL_Condition *cond);
```

## Function Parameters

|                                  |          |                                    |
| -------------------------------- | -------- | ---------------------------------- |
| [SDL_Condition](SDL_Condition) * | **cond** | the condition variable to destroy. |

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateCondition](SDL_CreateCondition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

