###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

## Version

This function is available since SDL 3.1.8.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

