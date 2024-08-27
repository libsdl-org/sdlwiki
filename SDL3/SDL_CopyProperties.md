###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CopyProperties

Copy a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
SDL_bool SDL_CopyProperties(SDL_PropertiesID src, SDL_PropertiesID dst);
```

## Function Parameters

|                                      |         |                             |
| ------------------------------------ | ------- | --------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **src** | the properties to copy.     |
| [SDL_PropertiesID](SDL_PropertiesID) | **dst** | the destination properties. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

Copy all the properties from one group of properties to another, with the
exception of properties requiring cleanup (set using
[SDL_SetPointerPropertyWithCleanup](SDL_SetPointerPropertyWithCleanup)()),
which will not be copied. Any property that already exists on `dst` will be
overwritten.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

