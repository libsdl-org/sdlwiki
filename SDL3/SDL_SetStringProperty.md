###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetStringProperty

Set a string property in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
bool SDL_SetStringProperty(SDL_PropertiesID props, const char *name, const char *value);
```

## Function Parameters

|                                      |           |                                                                |
| ------------------------------------ | --------- | -------------------------------------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to modify.                                      |
| const char *                         | **name**  | the name of the property to modify.                            |
| const char *                         | **value** | the new value of the property, or NULL to delete the property. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function makes a copy of the string; the caller does not have to
preserve the data after this call completes.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetStringProperty](SDL_GetStringProperty)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

