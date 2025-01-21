###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_DEPRECATED

A macro to tag a symbol as deprecated.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_DEPRECATED __attribute__((deprecated))
```

## Remarks

A function is marked deprecated by adding this macro to its declaration:

```c
extern SDL_DEPRECATED int ThisFunctionWasABadIdea(void);
```

Compilers with deprecation support can give a warning when a deprecated
function is used. This symbol may be used in SDL's headers, but apps are
welcome to use it for their own interfaces as well.

SDL, on occasion, might deprecate a function for various reasons. However,
SDL never removes symbols before major versions, so deprecated interfaces
in SDL3 will remain available until SDL4, where it would be expected an app
would have to take steps to migrate anyhow.

On compilers without a deprecation mechanism, this is defined to nothing,
and using a deprecated function will not generate a warning.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

