# CategoryIntrinsics

SDL does some preprocessor gymnastics to determine if any CPU-specific
compiler intrinsics are available, as this is not necessarily an easy thing
to calculate, and sometimes depends on quirks of a system, versions of
build tools, and other external forces.

Apps including SDL's headers will be able to check consistent preprocessor
definitions to decide if it's safe to use compiler intrinsics for a
specific CPU architecture. This check only tells you that the compiler is
capable of using those intrinsics; at runtime, you should still check if
they are available on the current system with the
[CPU info functions](https://wiki.libsdl.org/SDL3/CategoryCPUInfo)
, such as [SDL_HasSSE](SDL_HasSSE)() or [SDL_HasNEON](SDL_HasNEON)().
Otherwise, the process might crash for using an unsupported CPU
instruction.

SDL only sets preprocessor defines for CPU intrinsics if they are
supported, so apps should check with `#ifdef` and not `#if`.

SDL will also include the appropriate instruction-set-specific support
headers, so if SDL decides to define
[SDL_SSE2_INTRINSICS](SDL_SSE2_INTRINSICS), it will also `#include
<emmintrin.h>` as well.

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryIntrinsics, CategoryAPIFunction -->
- (none.)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryIntrinsics, CategoryAPIDatatype -->
- (none.)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryIntrinsics, CategoryAPIStruct -->
- (none.)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryIntrinsics, CategoryAPIEnum -->
- (none.)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryIntrinsics, CategoryAPIMacro -->
- [SDL_ALTIVEC_INTRINSICS](SDL_ALTIVEC_INTRINSICS)
- [SDL_AVX2_INTRINSICS](SDL_AVX2_INTRINSICS)
- [SDL_AVX512F_INTRINSICS](SDL_AVX512F_INTRINSICS)
- [SDL_AVX_INTRINSICS](SDL_AVX_INTRINSICS)
- [SDL_LASX_INTRINSICS](SDL_LASX_INTRINSICS)
- [SDL_LSX_INTRINSICS](SDL_LSX_INTRINSICS)
- [SDL_MMX_INTRINSICS](SDL_MMX_INTRINSICS)
- [SDL_NEON_INTRINSICS](SDL_NEON_INTRINSICS)
- [SDL_SSE2_INTRINSICS](SDL_SSE2_INTRINSICS)
- [SDL_SSE3_INTRINSICS](SDL_SSE3_INTRINSICS)
- [SDL_SSE4_1_INTRINSICS](SDL_SSE4_1_INTRINSICS)
- [SDL_SSE4_2_INTRINSICS](SDL_SSE4_2_INTRINSICS)
- [SDL_SSE_INTRINSICS](SDL_SSE_INTRINSICS)
- [SDL_TARGETING](SDL_TARGETING)
<!-- END CATEGORY LIST -->

----
[CategoryAPICategory](CategoryAPICategory)

