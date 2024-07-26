###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClaimTemporaryMemory

Claim ownership of temporary memory.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void * SDL_ClaimTemporaryMemory(const void *mem);
```

## Function Parameters

|              |         |                                                                                        |
| ------------ | ------- | -------------------------------------------------------------------------------------- |
| const void * | **mem** | a pointer allocated with [SDL_AllocateTemporaryMemory](SDL_AllocateTemporaryMemory)(). |

## Return Value

(void *) Returns a pointer to the memory now owned by the application,
which must be freed using [SDL_free](SDL_free)(), or NULL if the memory is
not in the temporary memory pool for the current thread.

## Remarks

This function removes memory from the temporary memory pool for the current
thread and gives ownership to the application. The application should use
[SDL_free](SDL_free)() to free it when it is done using it.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AllocateTemporaryMemory](SDL_AllocateTemporaryMemory)
- [SDL_free](SDL_free)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

