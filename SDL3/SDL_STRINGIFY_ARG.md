# SDL_STRINGIFY_ARG

Macro useful for building other macros with strings in them.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_STRINGIFY_ARG(arg)  #arg
```

## Macro Parameters

|         |                                         |
| ------- | --------------------------------------- |
| **arg** | the text to turn into a string literal. |

## Remarks

For example:

```c
#define LOG_ERROR(X) OutputDebugString(SDL_STRINGIFY_ARG(__FUNCTION__) ": " X "\n")`
```

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

