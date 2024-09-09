###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_static_cast

Handle a Static Cast properly whether using C or C++.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_static_cast(type, expression) static_cast<type>(expression)  /* or `((type)(expression))` in C */
```

## Macro Parameters

|                |                                             |
| -------------- | ------------------------------------------- |
| **type**       | the type to cast the expression to.         |
| **expression** | the expression to cast to a different type. |

## Return Value

Returns `expression`, cast to `type`.

## Remarks

If compiled as C++, this macro offers a proper C++ static_cast<>.

If compiled as C, this macro does a normal C-style cast.

This is helpful to avoid compiler warnings in C++.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.0.0.

## See Also

- [SDL_reinterpret_cast](SDL_reinterpret_cast)
- [SDL_const_cast](SDL_const_cast)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

