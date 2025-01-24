# SDL_GetStringProperty

Get a string property from a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
const char * SDL_GetStringProperty(SDL_PropertiesID props, const char *name, const char *default_value);
```

## Function Parameters

|                                      |                   |                                    |
| ------------------------------------ | ----------------- | ---------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props**         | the properties to query.           |
| const char *                         | **name**          | the name of the property to query. |
| const char *                         | **default_value** | the default value of the property. |

## Return Value

(const char *) Returns the value of the property, or `default_value` if it
is not set or not a string property.

## Thread Safety

It is safe to call this function from any thread, although the data
returned is not protected and could potentially be freed if you call
[SDL_SetStringProperty](SDL_SetStringProperty)() or
[SDL_ClearProperty](SDL_ClearProperty)() on these properties from another
thread. If you need to avoid this, use
[SDL_LockProperties](SDL_LockProperties)() and
[SDL_UnlockProperties](SDL_UnlockProperties)().

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetPropertyType](SDL_GetPropertyType)
- [SDL_HasProperty](SDL_HasProperty)
- [SDL_SetStringProperty](SDL_SetStringProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

