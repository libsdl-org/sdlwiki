###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetNumberProperty

Set an integer property on a set of properties 

## Syntax

```c
int SDL_SetNumberProperty(SDL_PropertiesID props, const char *name, Sint64 value);

```

## Function Parameters

|               |                                    |
| ------------- | ---------------------------------- |
| **props**     | the properties to modify           |
| **name**      | the name of the property to modify |
| **value**     | the new value of the property      |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumberProperty](SDL_GetNumberProperty)

----
[CategoryAPI](CategoryAPI)

