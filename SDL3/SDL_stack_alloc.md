# SDL_stack_alloc

Allocate memory on the stack (maybe).

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_stack_alloc(type, count)    (type*)alloca(sizeof(type)*(count))
```

## Macro Parameters

|           |                                           |
| --------- | ----------------------------------------- |
| **type**  | the datatype of the memory to allocate.   |
| **count** | the number of `type` objects to allocate. |

## Return Value

Returns newly-allocated memory, or NULL on failure.

## Remarks

If SDL knows how to access alloca() on the current platform, it will use it
to stack-allocate memory here. If it doesn't, it will use
[SDL_malloc](SDL_malloc)() to heap-allocate memory.

Since this might not be stack memory at all, it's important that you check
the returned pointer for NULL, and that you call
[SDL_stack_free](SDL_stack_free) on the memory when done with it. Since
this might be stack memory, it's important that you don't allocate large
amounts of it, or allocate in a loop without returning from the function,
so the stack doesn't overflow.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_stack_free](SDL_stack_free)






----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

