# SDL_copyp

A macro to copy memory between objects, with basic type checking.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_copyp(dst, src)                                                                 \
    { SDL_COMPILE_TIME_ASSERT(SDL_copyp, sizeof (*(dst)) == sizeof (*(src))); }             \
    SDL_memcpy((dst), (src), sizeof(*(src)))
```

## Macro Parameters

|         |                                                        |
| ------- | ------------------------------------------------------ |
| **dst** | a pointer to the destination object. Must not be NULL. |
| **src** | a pointer to the source object. Must not be NULL.      |

## Remarks

[SDL_memcpy](SDL_memcpy) and [SDL_memmove](SDL_memmove) do not care where
you copy memory to and from, which can lead to bugs. This macro aims to
avoid most of those bugs by making sure that the source and destination are
both pointers to objects that are the same size. It does not check that the
objects are the same _type_, just that the copy will not overflow either
object.

The size check happens at compile time, and the compiler will throw an
error if the objects are different sizes.

Generally this is intended to copy a single object, not an array.

This macro looks like it double-evaluates its parameters, but the extras
them are in `sizeof` sections, which generate no code nor side-effects.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

