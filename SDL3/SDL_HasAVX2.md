###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_HasAVX2

Determine whether the CPU has AVX2 features.

## Syntax

```c
SDL_bool SDL_HasAVX2(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has AVX2 features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasAVX](SDL_HasAVX)
* [SDL_HasAVX512F](SDL_HasAVX512F)

----
[CategoryAPI](CategoryAPI), [CategoryCPU](CategoryCPU), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


