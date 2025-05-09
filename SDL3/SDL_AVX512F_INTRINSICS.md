# SDL_AVX512F_INTRINSICS

Defined if (and only if) the compiler supports Intel AVX-512F intrinsics.

## Header File

Defined in [<SDL3/SDL_intrin.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_intrin.h)

## Syntax

```c
#define SDL_AVX512F_INTRINSICS 1
```

## Remarks

AVX-512F is also sometimes referred to as "AVX-512 Foundation."

If this macro is defined, SDL will have already included `<immintrin.h>`

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_AVX_INTRINSICS](SDL_AVX_INTRINSICS)
- [SDL_AVX2_INTRINSICS](SDL_AVX2_INTRINSICS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryIntrinsics](CategoryIntrinsics)

