# SDL_ALIGNED

A macro to specify data alignment.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_ALIGNED(x) __attribute__((aligned(x)))
```

## Macro Parameters

|       |                                                                                     |
| ----- | ----------------------------------------------------------------------------------- |
| **x** | the byte count to align to, so the data's address will be a multiple of this value. |

## Remarks

This informs the compiler that a given datatype or variable must be aligned
to a specific byte count.

For example:

```c
// make sure this is struct is aligned to 16 bytes for SIMD access.
typedef struct {
   float x, y, z, w;
} SDL_ALIGNED(16) MySIMDAlignedData;

// make sure this one field in a struct is aligned to 16 bytes for SIMD access.
typedef struct {
   SomeStuff stuff;
   float position[4] SDL_ALIGNED(16);
   SomeOtherStuff other_stuff;
} MyStruct;

// make sure this variable is aligned to 32 bytes.
int SDL_ALIGNED(32) myval = 0;
```

Alignment is only guaranteed for things the compiler places: local
variables on the stack and global/static variables. To dynamically allocate
something that respects this alignment, use
[SDL_aligned_alloc](SDL_aligned_alloc)() or some other mechanism.

On compilers without alignment support, this macro is defined to an invalid
symbol, to make it clear that the current compiler is likely to generate
incorrect code when it sees this macro.

## Version

This macro is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

