###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVersion

Get the version of SDL that is linked against your program.

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h)

## Syntax

```c
int SDL_GetVersion(SDL_Version * ver);

```

## Function Parameters

|             |                                                                                |
| ----------- | ------------------------------------------------------------------------------ |
| **ver**     | the [SDL_Version](SDL_Version) structure that contains the version information |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If you are linking to SDL dynamically, then it is possible that the current
version will be different than the version you compiled against. This
function returns the current version, while [SDL_VERSION](SDL_VERSION)() is
a macro that tells you what version you compiled with.

This function may be called safely at any time, even before
[SDL_Init](SDL_Init)().

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
SDL_Version compiled;
SDL_Version linked;

SDL_VERSION(&compiled);
SDL_GetVersion(&linked);
SDL_Log("We compiled against SDL version %u.%u.%u ...\n",
       compiled.major, compiled.minor, compiled.patch);
SDL_Log("But we are linking against SDL version %u.%u.%u.\n",
       linked.major, linked.minor, linked.patch);
```

## See Also

* [SDL_GetRevision](SDL_GetRevision)


## Related Macros

:[SDL_VERSION](SDL_VERSION)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVersion](CategoryVersion)


