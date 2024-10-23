###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_const_cast

Handle a Const Cast properly whether using C or C++.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_const_cast(type, expression) const_cast<type>(expression)  /* or `((type)(expression))` in C */
```

## Macro Parameters

|                |                                             |
| -------------- | ------------------------------------------- |
| **type**       | the type to cast the expression to.         |
| **expression** | the expression to cast to a different type. |

## Return Value

Returns `expression`, cast to `type`.

## Remarks

If compiled as C++, this macro offers a proper C++ const_cast<>.

If compiled as C, this macro does a normal C-style cast.

This is helpful to avoid compiler warnings in C++.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.1.3.

## See Also

- [SDL_reinterpret_cast](SDL_reinterpret_cast)
- [SDL_static_cast](SDL_static_cast)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

