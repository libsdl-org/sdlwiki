# SDL_GetRevision

Get the code revision of the SDL library that is linked against your program.

## Header File

Defined in [<SDL3/SDL_version.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h)

## Syntax

```c
const char * SDL_GetRevision(void);
```

## Return Value

(const char *) Returns an arbitrary string, uniquely identifying the exact
revision of the SDL library in use.

## Remarks

This value is the revision of the code you are linking against and may be
different from the code you are compiling with, which is found in the
constant [SDL_REVISION](SDL_REVISION).

The revision is an arbitrary string (a hash value) uniquely identifying the
exact revision of the SDL library in use, and is only useful in comparing
against other revisions. It is NOT an incrementing number.

If SDL wasn't built from a git repository with the appropriate tools, this
will return an empty string.

You shouldn't use this function for anything but logging it for debugging
purposes. The string is not intended to be reliable in any way.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetVersion](SDL_GetVersion)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVersion](CategoryVersion)

