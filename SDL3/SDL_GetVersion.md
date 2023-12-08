###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVersion

Get the version of SDL that is linked against your program.

## Syntax

```c
int SDL_GetVersion(SDL_version * ver);

```

## Function Parameters

|             |                                                                                |
| ----------- | ------------------------------------------------------------------------------ |
| **ver**     | the [SDL_version](SDL_version.md) structure that contains the version information |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

If you are linking to SDL dynamically, then it is possible that the current
version will be different than the version you compiled against. This
function returns the current version, while [SDL_VERSION](SDL_VERSION.md)() is
a macro that tells you what version you compiled with.

This function may be called safely at any time, even before
[SDL_Init](SDL_Init.md)().

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
SDL_version compiled;
SDL_version linked;

SDL_VERSION(&compiled);
SDL_GetVersion(&linked);
SDL_Log("We compiled against SDL version %u.%u.%u ...\n",
       compiled.major, compiled.minor, compiled.patch);
SDL_Log("But we are linking against SDL version %u.%u.%u.\n",
       linked.major, linked.minor, linked.patch);
```

## Related Functions

* [SDL_GetRevision](SDL_GetRevision.md)


## Related Macros

:[SDL_VERSION](SDL_VERSION.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVersion](CategoryVersion.md)
