###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetFloatProperty

Get a floating point property on a set of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
float SDL_GetFloatProperty(SDL_PropertiesID props, const char *name, float default_value);
```

## Function Parameters

|                                      |                   |                                   |
| ------------------------------------ | ----------------- | --------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props**         | the properties to query           |
| const char *                         | **name**          | the name of the property to query |
| float                                | **default_value** | the default value of the property |

## Return Value

(float) Returns the value of the property, or `default_value` if it is not
set or not a float property.

## Remarks

You can use [SDL_GetPropertyType](SDL_GetPropertyType)() to query whether
the property exists and is a floating point property.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetPropertyType](SDL_GetPropertyType)
- [SDL_HasProperty](SDL_HasProperty)
- [SDL_SetFloatProperty](SDL_SetFloatProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

