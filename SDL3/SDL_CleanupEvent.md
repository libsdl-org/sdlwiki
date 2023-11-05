###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CleanupEvent

Clean up dynamically allocated memory for an event.

## Syntax

```c
void SDL_CleanupEvent(SDL_Event *event);

```

## Function Parameters

|               |                                                  |
| ------------- | ------------------------------------------------ |
| **event**     | a pointer to the event that should be cleaned up |

## Remarks

Some events have dynamically allocated data that must be cleaned up when
the event is processed. If you handle any of these events, you should call
[SDL_CleanupEvent](SDL_CleanupEvent)() after processing them:
[SDL_EVENT_DROP_FILE](SDL_EVENT_DROP_FILE)
[SDL_EVENT_DROP_TEXT](SDL_EVENT_DROP_TEXT)
[SDL_EVENT_SYSWM](SDL_EVENT_SYSWM)
[SDL_EVENT_TEXT_EDITING](SDL_EVENT_TEXT_EDITING)

It is safe, but not necessary, to call this function for other event types.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_PollEvent](SDL_PollEvent)
* [SDL_WaitEvent](SDL_WaitEvent)
* [SDL_WaitEventTimeout](SDL_WaitEventTimeout)

----
[CategoryAPI](CategoryAPI)

