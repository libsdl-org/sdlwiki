# SDL_HAS_EXTENSION

Check if the compiler supports a given extension.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_HAS_EXTENSION(x) __has_extension(x)
```

## Remarks

This allows preprocessor checks for things that otherwise might fail to
compile.

Supported by virtually all clang versions and more-recent GCCs. Use this
instead of checking the clang version if possible.

On compilers without has_extension support, this is defined to 0 (always
false).

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

