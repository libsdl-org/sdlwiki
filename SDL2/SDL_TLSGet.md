###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TLSGet

Get the current thread's value associated with a thread local storage ID.

## Syntax

```c
void * SDL_TLSGet(SDL_TLSID id);

```

## Function Parameters

|            |                             |
| ---------- | --------------------------- |
| **id**     | the thread local storage ID |

## Return Value

Returns the value associated with the ID for the current thread or NULL if
no value has been set; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_TLSCreate](SDL_TLSCreate)
* [SDL_TLSSet](SDL_TLSSet)

----
[CategoryAPI](CategoryAPI)

