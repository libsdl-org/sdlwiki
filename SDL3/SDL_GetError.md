###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetError

Retrieve a message about the last error that occurred on the current thread.

## Header File

Defined in [<SDL3/SDL_error.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h)

## Syntax

```c
const char * SDL_GetError(void);
```

## Return Value

(const char *) Returns a message with information about the specific error
that occurred, or an empty string if there hasn't been an error message set
since the last call to [SDL_ClearError](SDL_ClearError)().

## Remarks

It is possible for multiple errors to occur before calling
[SDL_GetError](SDL_GetError)(). Only the last error is returned.

The message is only applicable when an SDL function has signaled an error.
You must check the return values of SDL function calls to determine when to
appropriately call [SDL_GetError](SDL_GetError)(). You should *not* use the
results of [SDL_GetError](SDL_GetError)() to decide if an error has
occurred! Sometimes SDL will set an error string even when reporting
success.

SDL will *not* clear the error string for successful API calls. You *must*
check return values for failure cases before you can assume the error
string applies.

Error strings are set per-thread, so an error set in a different thread
will not interfere with the current thread's operation.

The returned value is a thread-local string which will remain valid until
the current thread's error string is changed. The caller should make a copy
if the value is needed after the next SDL API call.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
if (SDL_Init(SDL_INIT_VIDEO) < 0) {
    // Unrecoverable error, exit here.
    printf("SDL_Init failed: %s\n", SDL_GetError());
}
```
Note: Although this example uses [SDL_Init](SDL_Init)(), [SDL_GetError](SDL_GetError)() provides an error message for any failed SDL operation which supports error reporting, see the wiki page for each particular SDL function.

## See Also

- [SDL_ClearError](SDL_ClearError)
- [SDL_SetError](SDL_SetError)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryError](CategoryError)

