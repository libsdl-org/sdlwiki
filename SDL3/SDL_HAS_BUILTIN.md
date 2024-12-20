###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HAS_BUILTIN

Check if the compiler supports a given builtin functionality.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_HAS_BUILTIN(x) __has_builtin(x)
```

## Remarks

This allows preprocessor checks for things that otherwise might fail to
compile.

Supported by virtually all clang versions and more-recent GCCs. Use this
instead of checking the clang version if possible.

On compilers without has_builtin support, this is defined to 0 (always
false).

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

