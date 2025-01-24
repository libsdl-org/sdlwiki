# SDL_NEON_INTRINSICS

Defined if (and only if) the compiler supports ARM NEON intrinsics.

## Header File

Defined in [<SDL3/SDL_intrin.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_intrin.h)

## Syntax

```c
#define SDL_NEON_INTRINSICS 1
```

## Remarks

If this macro is defined, SDL will have already included `<armintr.h>`
`<arm_neon.h>`, `<arm64intr.h>`, and `<arm64_neon.h>`, as appropriate.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryIntrinsics](CategoryIntrinsics)

