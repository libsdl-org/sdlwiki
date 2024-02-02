###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CopyProperties

Copy a set of properties 

## Syntax

```c
int SDL_CopyProperties(SDL_PropertiesID src, SDL_PropertiesID dst);

```

## Function Parameters

|             |                            |
| ----------- | -------------------------- |
| **src**     | the properties to copy     |
| **dst**     | the destination properties |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Copy all the properties from one set of properties to another, with the
exception of properties requiring cleanup (set using
[SDL_SetPropertyWithCleanup](SDL_SetPropertyWithCleanup)()), which will not
be copied. Any property that already exists on `dst` will be overwritten.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

