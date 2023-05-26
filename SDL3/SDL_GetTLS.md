###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTLS

Get the current thread's value associated with a thread local storage ID.

## Syntax

```c
void * SDL_GetTLS(SDL_TLSID id);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateTLS](SDL_CreateTLS)
* [SDL_SetTLS](SDL_SetTLS)

----
[CategoryAPI](CategoryAPI)

