###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SSE_INTRINSICS

Defined if (and only if) the compiler supports Intel SSE intrinsics.

## Header File

Defined in [<SDL3/SDL_intrin.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_intrin.h)

## Syntax

```c
#define SDL_SSE_INTRINSICS 1
```

## Remarks

If this macro is defined, SDL will have already included `<xmmintrin.h>`

## Version

This macro is available since 3.1.3.

## See Also

- [SDL_SSE2_INTRINSICS](SDL_SSE2_INTRINSICS)
- [SDL_SSE3_INTRINSICS](SDL_SSE3_INTRINSICS)
- [SDL_SSE4_1_INTRINSICS](SDL_SSE4_1_INTRINSICS)
- [SDL_SSE4_2_INTRINSICS](SDL_SSE4_2_INTRINSICS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryIntrinsics](CategoryIntrinsics)

