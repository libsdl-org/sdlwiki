###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumberProperty

Get a number property on a set of properties 

## Syntax

```c
Sint64 SDL_GetNumberProperty(SDL_PropertiesID props, const char *name, Sint64 default_value);

```

## Function Parameters

|                       |                                   |
| --------------------- | --------------------------------- |
| **props**             | the properties to query           |
| **name**              | the name of the property to query |
| **default_value**     | the default value of the property |

## Return Value

Returns the value of the property, or `default_value` if it is not set or
not a number property.

## Remarks

You can use [SDL_GetPropertyType](SDL_GetPropertyType)() to query whether
the property exists and is a number property.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetPropertyType](SDL_GetPropertyType)
* [SDL_SetNumberProperty](SDL_SetNumberProperty)

----
[CategoryAPI](CategoryAPI)

