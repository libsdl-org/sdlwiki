# SDL_RunOnMainThread

Call a function on the main thread during event processing.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
bool SDL_RunOnMainThread(SDL_MainThreadCallback callback, void *userdata, bool wait_complete);
```

## Function Parameters

|                                                  |                   |                                                                         |
| ------------------------------------------------ | ----------------- | ----------------------------------------------------------------------- |
| [SDL_MainThreadCallback](SDL_MainThreadCallback) | **callback**      | the callback to call on the main thread.                                |
| void *                                           | **userdata**      | a pointer that is passed to `callback`.                                 |
| bool                                             | **wait_complete** | true to wait for the callback to complete, false to return immediately. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If this is called on the main thread, the callback is executed immediately.
If this is called on another thread, this callback is queued for execution
on the main thread during event processing.

Be careful of deadlocks when using this functionality. You should not have
the main thread wait for the current thread while this function is being
called with `wait_complete` true.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_IsMainThread](SDL_IsMainThread)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)

