###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTLS

Get the current thread's value associated with a thread local storage ID.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
void * SDL_GetTLS(SDL_TLSID *id);
```

## Function Parameters

|                          |        |                                                            |
| ------------------------ | ------ | ---------------------------------------------------------- |
| [SDL_TLSID](SDL_TLSID) * | **id** | a pointer to the thread local storage ID, may not be NULL. |

## Return Value

(void *) Returns the value associated with the ID for the current thread or
NULL if no value has been set; call [SDL_GetError](SDL_GetError)() for more
information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetTLS](SDL_SetTLS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

