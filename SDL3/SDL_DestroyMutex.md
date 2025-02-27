# SDL_DestroyMutex

Destroy a mutex created with [SDL_CreateMutex](SDL_CreateMutex)().

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_DestroyMutex(SDL_Mutex *mutex);
```

## Function Parameters

|                          |           |                       |
| ------------------------ | --------- | --------------------- |
| [SDL_Mutex](SDL_Mutex) * | **mutex** | the mutex to destroy. |

## Remarks

This function must be called on any mutex that is no longer needed. Failure
to destroy a mutex will result in a system memory or resource leak. While
it is safe to destroy a mutex that is _unlocked_, it is not safe to attempt
to destroy a locked mutex, and may result in undefined behavior depending
on the platform.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateMutex](SDL_CreateMutex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

