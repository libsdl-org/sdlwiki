###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRevision

Get the code revision of SDL that is linked against your program.

## Syntax

```c
const char* SDL_GetRevision(void);

```

## Return Value

Returns an arbitrary string, uniquely identifying the exact revision of the
SDL library in use.

## Remarks

This value is the revision of the code you are linked with and may be
different from the code you are compiling with, which is found in the
constant [SDL_REVISION](SDL_REVISION.md).

The revision is arbitrary string (a hash value) uniquely identifying the
exact revision of the SDL library in use, and is only useful in comparing
against other revisions. It is NOT an incrementing number.

If SDL wasn't built from a git repository with the appropriate tools, this
will return an empty string.

Prior to SDL 2.0.16, before development moved to GitHub, this returned a
hash for a Mercurial repository.

You shouldn't use this function for anything but logging it for debugging
purposes. The string is not intended to be reliable in any way.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetVersion](SDL_GetVersion.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVersion](CategoryVersion.md)
