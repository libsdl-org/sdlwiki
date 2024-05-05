###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateProperties

Create a set of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
SDL_PropertiesID SDL_CreateProperties(void);

```

## Return Value

Returns an ID for a new set of properties, or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

All properties are automatically destroyed when [SDL_Quit](SDL_Quit)() is
called.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_DestroyProperties](SDL_DestroyProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

