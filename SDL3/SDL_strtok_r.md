###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_strtok_r

This works exactly like strtok_r() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_strtok_r(char *str, const char *delim, char **saveptr);
```

## Function Parameters

|              |             |                                                         |
| ------------ | ----------- | ------------------------------------------------------- |
| char *       | **str**     | the string to tokenize, or NULL to continue tokenizing. |
| const char * | **delim**   | the delimiter string that separates tokens.             |
| char **      | **saveptr** | pointer to a char *, used for ongoing state.            |

## Return Value

(char *) Returns A pointer to the next token, or NULL if no tokens remain.

## Remarks

Break a string up into a series of tokens.

To start tokenizing a new string, `str` should be the non-NULL address of
the string to start tokenizing. Future calls to get the next token from the
same string should specify a NULL.

Note that this function will overwrite pieces of `str` with null chars to
split it into tokens. This function cannot be used with const/read-only
strings!

`saveptr` just needs to point to a `char *` that can be overwritten; SDL
will use this to save tokenizing state between calls. It is initialized if
`str` is non-NULL, and used to resume tokenizing when `str` is NULL.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

