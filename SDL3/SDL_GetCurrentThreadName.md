# SDL_GetCurrentThreadName

Get the thread name for the current thread.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
const char * SDL_GetCurrentThreadName(void);
```

## Return Value

(const char *) Returns the name of the current thread, or NULL if not
available.

## Remarks

Thread names are always available for threads started through
[SDL_CreateThread](SDL_CreateThread)() or
[SDL_CreateThreadWithProperties](SDL_CreateThreadWithProperties)(). For
other threads, SDL will query the OS if possible. This is not possible on
every platform, and will return NULL in these cases.

On supported platforms, and for SDL-created threads, this might still
return NULL if there was an error, or the system is out of memory, etc.

The returned string is owned by SDL and guaranteed to live until the
calling thread terminates. If it needs to be passed to another thread that
might outlive the caller's thread, you should make a copy of the string.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_GetThreadName](SDL_GetThreadName)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

