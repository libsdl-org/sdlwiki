###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTLS

Get the current thread's value associated with a thread local storage ID.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h), but apps should use `#include <SDL3/SDL.h>`

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

## See Also

* [SDL_SetTLS](SDL_SetTLS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

