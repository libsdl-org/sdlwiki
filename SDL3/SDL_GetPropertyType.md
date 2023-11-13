###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPropertyType

Get the type of a property on a set of properties 

## Syntax

```c
SDL_PropertyType SDL_GetPropertyType(SDL_PropertiesID props, const char *name);

```

## Function Parameters

|               |                                   |
| ------------- | --------------------------------- |
| **props**     | the properties to query           |
| **name**      | the name of the property to query |

## Return Value

Returns the type of the property, or
[SDL_PROPERTY_TYPE_INVALID](SDL_PROPERTY_TYPE_INVALID) if it is not set.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

