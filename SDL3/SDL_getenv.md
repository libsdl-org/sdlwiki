# SDL_getenv

Get the value of a variable in the environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
const char * SDL_getenv(const char *name);
```

## Function Parameters

|              |          |                                  |
| ------------ | -------- | -------------------------------- |
| const char * | **name** | the name of the variable to get. |

## Return Value

(const char *) Returns a pointer to the value of the variable or NULL if it
can't be found.

## Remarks

The name of the variable is case sensitive on all platforms.

This function uses SDL's cached copy of the environment and is thread-safe.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

