###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RETURN_CAPABILITY

Wrapper around Clang thread safety analysis annotations.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
#define SDL_RETURN_CAPABILITY(x) \
  SDL_THREAD_ANNOTATION_ATTRIBUTE__(lock_returned(x))
```

## Remarks

Please see https://clang.llvm.org/docs/ThreadSafetyAnalysis.html#mutex-h

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMutex](CategoryMutex)

