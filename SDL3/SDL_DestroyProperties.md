###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyProperties

Destroy a set of properties 

## Syntax

```c
void SDL_DestroyProperties(SDL_PropertiesID props);

```

## Function Parameters

|               |                           |
| ------------- | ------------------------- |
| **props**     | the properties to destroy |

## Remarks

All properties are deleted and their cleanup functions will be called, if
any.

## Thread Safety

This function should not be called while these properties are locked or
other threads might be setting or getting values from these properties.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateProperties](SDL_CreateProperties)

----
[CategoryAPI](CategoryAPI)

