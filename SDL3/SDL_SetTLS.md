###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetTLS

Set the current thread's value associated with a thread local storage ID.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
int SDL_SetTLS(SDL_TLSID id, const void *value, SDL_TLSDestructorCallback destructor);
```

## Function Parameters

|                                                        |                |                                                                          |
| ------------------------------------------------------ | -------------- | ------------------------------------------------------------------------ |
| [SDL_TLSID](SDL_TLSID)                                 | **id**         | the thread local storage ID.                                             |
| const void *                                           | **value**      | the value to associate with the ID for the current thread.               |
| [SDL_TLSDestructorCallback](SDL_TLSDestructorCallback) | **destructor** | a function called when the thread exits, to free the value. Can be NULL. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Note that replacing a value from a previous call to this function on the
same thread does _not_ call the previous value's destructor!

`destructor` can be NULL; it is assumed that `value` does not need to be
cleaned up if so.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetTLS](SDL_GetTLS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

