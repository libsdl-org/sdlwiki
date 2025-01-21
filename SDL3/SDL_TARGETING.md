###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_TARGETING

A macro to tag a function as targeting a specific CPU architecture.

## Header File

Defined in [<SDL3/SDL_intrin.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_intrin.h)

## Syntax

```c
#define SDL_TARGETING(x) __attribute__((target(x)))
```

## Remarks

This is a hint to the compiler that a function should be built with support
for a CPU instruction set that might be different than the rest of the
program.

The particulars of this are explained in the GCC documentation:

https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html#index-target-function-attribute

An example of using this feature is to turn on SSE2 support for a specific
function, even if the rest of the source code is not compiled to use SSE2
code:

```c
#ifdef SDL_SSE2_INTRINSICS
static void SDL_TARGETING("sse2") DoSomethingWithSSE2(char *x) {
   ...use SSE2 intrinsic functions, etc...
}
#endif

// later...
#ifdef SDL_SSE2_INTRINSICS
if (SDL_HasSSE2()) {
    DoSomethingWithSSE2(str);
}
#endif
```

The application is, on a whole, built without SSE2 instructions, so it will
run on Intel machines that don't support SSE2. But then at runtime, it
checks if the system supports the instructions, and then calls into a
function that uses SSE2 opcodes. The ifdefs make sure that this code isn't
used on platforms that don't have SSE2 at all.

On compilers without target support, this is defined to nothing.

This symbol is used by SDL internally, but apps and other libraries are
welcome to use it for their own interfaces as well.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryIntrinsics](CategoryIntrinsics)

