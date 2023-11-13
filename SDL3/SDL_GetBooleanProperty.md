###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetBooleanProperty

Get a boolean property on a set of properties 

## Syntax

```c
SDL_bool SDL_GetBooleanProperty(SDL_PropertiesID props, const char *name, SDL_bool default_value);

```

## Function Parameters

|                       |                                   |
| --------------------- | --------------------------------- |
| **props**             | the properties to query           |
| **name**              | the name of the property to query |
| **default_value**     | the default value of the property |

## Return Value

Returns the value of the property, or `default_value` if it is not set or
not a float property.

## Remarks

You can use [SDL_GetPropertyType](SDL_GetPropertyType)() to query whether
the property exists and is a boolean property.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetPropertyType](SDL_GetPropertyType)
* [SDL_SetBooleanProperty](SDL_SetBooleanProperty)

----
[CategoryAPI](CategoryAPI)

