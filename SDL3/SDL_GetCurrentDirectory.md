# SDL_GetCurrentDirectory

Get what the system believes is the "current working directory."

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
char * SDL_GetCurrentDirectory(void);
```

## Return Value

(char *) Returns a UTF-8 string of the current working directory in
platform-dependent notation. NULL if there's a problem. This should be
freed with [SDL_free](SDL_free)() when it is no longer needed.

## Remarks

For systems without a concept of a current working directory, this will
still attempt to provide something reasonable.

SDL does not provide a means to _change_ the current working directory; for
platforms without this concept, this would cause surprises with file access
outside of SDL.

The returned path is guaranteed to end with a path separator ('\\' on
Windows, '/' on most other platforms).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

