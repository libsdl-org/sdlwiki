###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetFloatProperty

Set a floating point property in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
SDL_bool SDL_SetFloatProperty(SDL_PropertiesID props, const char *name, float value);
```

## Function Parameters

|                                      |           |                                     |
| ------------------------------------ | --------- | ----------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to modify.           |
| const char *                         | **name**  | the name of the property to modify. |
| float                                | **value** | the new value of the property.      |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetFloatProperty](SDL_GetFloatProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

