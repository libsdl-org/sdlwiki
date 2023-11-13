###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EnumerateProperties

Enumerate the properties on a set of properties 

## Syntax

```c
int SDL_EnumerateProperties(SDL_PropertiesID props, SDL_EnumeratePropertiesCallback callback, void *userdata);

```

## Function Parameters

|                  |                                        |
| ---------------- | -------------------------------------- |
| **props**        | the properties to query                |
| **callback**     | the function to call for each property |
| **userdata**     | a pointer that is passed to `callback` |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The callback function is called for each property on the set of properties.
The properties are locked during enumeration.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

