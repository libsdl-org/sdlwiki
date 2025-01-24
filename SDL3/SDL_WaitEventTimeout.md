# SDL_WaitEventTimeout

Wait until the specified timeout (in milliseconds) for the next available event.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
bool SDL_WaitEventTimeout(SDL_Event *event, Sint32 timeoutMS);
```

## Function Parameters

|                          |               |                                                                                                   |
| ------------------------ | ------------- | ------------------------------------------------------------------------------------------------- |
| [SDL_Event](SDL_Event) * | **event**     | the [SDL_Event](SDL_Event) structure to be filled in with the next event from the queue, or NULL. |
| [Sint32](Sint32)         | **timeoutMS** | the maximum number of milliseconds to wait for the next available event.                          |

## Return Value

(bool) Returns true if this got an event or false if the timeout elapsed
without any events available.

## Remarks

If `event` is not NULL, the next event is removed from the queue and stored
in the [SDL_Event](SDL_Event) structure pointed to by `event`.

As this function may implicitly call [SDL_PumpEvents](SDL_PumpEvents)(),
you can only call this function in the thread that initialized the video
subsystem.

The timeout is not guaranteed, the actual wait time could be longer due to
system scheduling.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PollEvent](SDL_PollEvent)
- [SDL_PushEvent](SDL_PushEvent)
- [SDL_WaitEvent](SDL_WaitEvent)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

