# SDL_GetWindowFromEvent

Get window associated with an event.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
SDL_Window * SDL_GetWindowFromEvent(const SDL_Event *event);
```

## Function Parameters

|                                |           |                                   |
| ------------------------------ | --------- | --------------------------------- |
| const [SDL_Event](SDL_Event) * | **event** | an event containing a `windowID`. |

## Return Value

([SDL_Window](SDL_Window) *) Returns the associated window on success or
NULL if there is none.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PollEvent](SDL_PollEvent)
- [SDL_WaitEvent](SDL_WaitEvent)
- [SDL_WaitEventTimeout](SDL_WaitEventTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

