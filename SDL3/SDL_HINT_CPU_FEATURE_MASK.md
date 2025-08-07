# SDL_HINT_CPU_FEATURE_MASK

A variable that limits what CPU features are available.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_CPU_FEATURE_MASK "SDL_CPU_FEATURE_MASK"
```

## Remarks

By default, SDL marks all features the current CPU supports as available.
This hint allows the enabled features to be limited to a subset.

When the hint is unset, or empty, SDL will enable all detected CPU
features.

The variable can be set to a comma separated list containing the following
items:

- "all"
- "altivec"
- "sse"
- "sse2"
- "sse3"
- "sse41"
- "sse42"
- "avx"
- "avx2"
- "avx512f"
- "arm-simd"
- "neon"
- "lsx"
- "lasx"

The items can be prefixed by '+'/'-' to add/remove features.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

