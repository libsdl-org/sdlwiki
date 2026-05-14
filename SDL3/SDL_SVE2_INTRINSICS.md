# SDL_SVE2_INTRINSICS

Defined if (and only if) the compiler supports ARM SVE2 intrinsics.

## Header File

Defined in [<SDL3/SDL_intrin.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_intrin.h)

## Syntax

```c
#define SDL_SVE2_INTRINSICS 1
```

## Remarks

If this macro is defined, SDL will have already included `<arm_sve.h>` as
appropriate.

## Version

This macro is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryIntrinsics](CategoryIntrinsics)

