# SDL_REQUIRES_SHARED

Wrapper around Clang thread safety analysis annotations.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
#define SDL_REQUIRES_SHARED(x) \
  SDL_THREAD_ANNOTATION_ATTRIBUTE__(requires_shared_capability(x))
```

## Remarks

Please see https://clang.llvm.org/docs/ThreadSafetyAnalysis.html#mutex-h

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMutex](CategoryMutex)

