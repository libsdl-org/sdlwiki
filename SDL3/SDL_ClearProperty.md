###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClearProperty

Clear a property on a set of properties 

## Syntax

```c
int SDL_ClearProperty(SDL_PropertiesID props, const char *name);

```

## Function Parameters

|               |                                   |
| ------------- | --------------------------------- |
| **props**     | the properties to modify          |
| **name**      | the name of the property to clear |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)

----
[CategoryAPI](CategoryAPI)

