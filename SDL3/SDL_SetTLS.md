###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetTLS

Set the current thread's value associated with a thread local storage ID.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_SetTLS(SDL_TLSID id, const void *value, void (SDLCALL *destructor)(void*));

```

## Function Parameters

|                    |                                                            |
| ------------------ | ---------------------------------------------------------- |
| **id**             | the thread local storage ID                                |
| **value**          | the value to associate with the ID for the current thread  |
| **destructor**     | a function called when the thread exits, to free the value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The function prototype for `destructor` is:

```c
void destructor(void *value)
```

where its parameter `value` is what was passed as `value` to
[SDL_SetTLS](SDL_SetTLS)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetTLS](SDL_GetTLS)

----
[CategoryAPI](CategoryAPI)

