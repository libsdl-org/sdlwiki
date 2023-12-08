###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRevisionNumber

Obsolete function, do not use.

## Deprecated

Use [SDL_GetRevision](SDL_GetRevision.md)() instead; if SDL was carefully
built, it will return a git hash.

## Syntax

```c
int SDL_GetRevisionNumber(void);

```

## Return Value

Returns zero, always, in modern SDL releases.

## Remarks

When SDL was hosted in a Mercurial repository, and was built carefully,
this would return the revision number that the build was created from. This
number was not reliable for several reasons, but more importantly, SDL is
now hosted in a git repository, which does not offer numbers at all, only
hashes. This function only ever returns zero now. Don't use it.

Before SDL 2.0.16, this might have returned an unreliable, but non-zero
number.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetRevision](SDL_GetRevision.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVersion](CategoryVersion.md)
