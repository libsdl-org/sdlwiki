###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TLSGet

Get the current thread's value associated with a thread local storage ID.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_thread.h)

## Syntax

```c
void * SDL_TLSGet(SDL_TLSID id);
```

## Function Parameters

|                        |        |                             |
| ---------------------- | ------ | --------------------------- |
| [SDL_TLSID](SDL_TLSID) | **id** | the thread local storage ID |

## Return Value

(void *) Returns the value associated with the ID for the current thread or
NULL if no value has been set; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_TLSCreate](SDL_TLSCreate)
- [SDL_TLSSet](SDL_TLSSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

