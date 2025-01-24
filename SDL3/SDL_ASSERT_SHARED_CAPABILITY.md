# SDL_ASSERT_SHARED_CAPABILITY

Wrapper around Clang thread safety analysis annotations.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
#define SDL_ASSERT_SHARED_CAPABILITY(x) \
  SDL_THREAD_ANNOTATION_ATTRIBUTE__(assert_shared_capability(x))
```

## Remarks

Please see https://clang.llvm.org/docs/ThreadSafetyAnalysis.html#mutex-h

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMutex](CategoryMutex)

