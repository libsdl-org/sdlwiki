###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAssertionHandler

Set an application-defined assertion handler.

## Syntax

```c
void SDL_SetAssertionHandler(
                    SDL_AssertionHandler handler,
                    void *userdata);

```

## Function Parameters

|                  |                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **handler**      | the [SDL_AssertionHandler](SDL_AssertionHandler.md) function to call when an assertion fails or NULL for the default handler |
| **userdata**     | a pointer that is passed to `handler`                                                                                     |

## Remarks

This function allows an application to show its own assertion UI and/or
force the response to an assertion failure. If the application doesn't
provide this, SDL will try to do the right thing, popping up a
system-specific GUI dialog, and probably minimizing any fullscreen windows.

This callback may fire from any thread, but it runs wrapped in a mutex, so
it will only fire from one thread at a time.

This callback is NOT reset to SDL's internal handler upon
[SDL_Quit](SDL_Quit.md)()!

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetAssertionHandler](SDL_GetAssertionHandler.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAssertions](CategoryAssertions.md)
