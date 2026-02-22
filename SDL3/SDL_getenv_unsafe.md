# SDL_getenv_unsafe

Get the value of a variable in the environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
const char * SDL_getenv_unsafe(const char *name);
```

## Function Parameters

|              |          |                                  |
| ------------ | -------- | -------------------------------- |
| const char * | **name** | the name of the variable to get. |

## Return Value

(const char *) Returns a pointer to the value of the variable or NULL if it
can't be found.

## Remarks

This function bypasses SDL's cached copy of the environment and is not
thread-safe.

On some platforms, this may make case-insensitive matches, while other
platforms are case-sensitive. It is best to be precise with strings used
for queries through this interface. [SDL_getenv](SDL_getenv) is always
case-sensitive, however.

## Thread Safety

This function is not thread safe, consider using [SDL_getenv](SDL_getenv)()
instead.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_getenv](SDL_getenv)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

