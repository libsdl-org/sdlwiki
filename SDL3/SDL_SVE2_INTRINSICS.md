# SDL_SVE2_INTRINSICS

Defined if (and only if) the compiler supports ARM SVE2 intrinsics.

## Header File

Defined in [<SDL3/SDL_intrin.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_intrin.h)

## Syntax

```c
#define SDL_SVE2_INTRINSICS 1
```

## Remarks

If this macro is defined, `<arm_sve.h>` (providing SVE intrinsics) will
only be included if the target architecture supports SVE
(`__ARM_FEATURE_SVE` feature macro). Some toolchains do not support
`SDL_TARGETING("arch=armv8-a+sve2")`, so for best portability you need to
write all SVE code in a separate translation unit and add appropriate
compile flags.

## Version

This macro is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryIntrinsics](CategoryIntrinsics)

