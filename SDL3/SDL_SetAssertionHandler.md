# SDL_SetAssertionHandler

Set an application-defined assertion handler.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
void SDL_SetAssertionHandler(
                SDL_AssertionHandler handler,
                void *userdata);
```

## Function Parameters

|                                              |              |                                                                                                                            |
| -------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| [SDL_AssertionHandler](SDL_AssertionHandler) | **handler**  | the [SDL_AssertionHandler](SDL_AssertionHandler) function to call when an assertion fails or NULL for the default handler. |
| void *                                       | **userdata** | a pointer that is passed to `handler`.                                                                                     |

## Remarks

This function allows an application to show its own assertion UI and/or
force the response to an assertion failure. If the application doesn't
provide this, SDL will try to do the right thing, popping up a
system-specific GUI dialog, and probably minimizing any fullscreen windows.

This callback may fire from any thread, but it runs wrapped in a mutex, so
it will only fire from one thread at a time.

This callback is NOT reset to SDL's internal handler upon
[SDL_Quit](SDL_Quit)()!

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetAssertionHandler](SDL_GetAssertionHandler)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAssert](CategoryAssert)

