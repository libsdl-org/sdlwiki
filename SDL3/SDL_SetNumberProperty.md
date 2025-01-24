# SDL_SetNumberProperty

Set an integer property in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
bool SDL_SetNumberProperty(SDL_PropertiesID props, const char *name, Sint64 value);
```

## Function Parameters

|                                      |           |                                     |
| ------------------------------------ | --------- | ----------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to modify.           |
| const char *                         | **name**  | the name of the property to modify. |
| [Sint64](Sint64)                     | **value** | the new value of the property.      |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetNumberProperty](SDL_GetNumberProperty)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

