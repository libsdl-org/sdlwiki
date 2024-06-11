###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasProperty

Return whether a property exists in a set of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
SDL_bool SDL_HasProperty(SDL_PropertiesID props, const char *name);
```

## Function Parameters

|               |                                   |
| ------------- | --------------------------------- |
| **props**     | the properties to query           |
| **name**      | the name of the property to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the property exists, or
[SDL_FALSE](SDL_FALSE) if it doesn't.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetPropertyType](SDL_GetPropertyType)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

