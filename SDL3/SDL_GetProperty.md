###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetProperty

Get a property on a set of properties 

## Syntax

```c
void* SDL_GetProperty(SDL_PropertiesID props, const char *name);

```

## Function Parameters

|               |                                   |
| ------------- | --------------------------------- |
| **props**     | the properties to query           |
| **name**      | the name of the property to query |

## Return Value

Returns the value of the property, or NULL if it is not set.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

