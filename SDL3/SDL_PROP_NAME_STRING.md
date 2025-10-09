# SDL_PROP_NAME_STRING

A generic property for naming things.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
#define SDL_PROP_NAME_STRING "SDL.name"
```

## Remarks

This property is intended to be added to any property set that needs the
set named, or needs a generic name for the object that the properties are
associated with. It is not guaranteed that any property set will include
this property, but it is convenient to have a standard property name that
any piece of code could reasonable agree to use.

There is no format for the value set with this key; it is expected to be
human-readable.

## Version

This macro is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryProperties](CategoryProperties)

