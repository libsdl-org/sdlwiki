###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasProperty

Return whether a property exists in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
bool SDL_HasProperty(SDL_PropertiesID props, const char *name);
```

## Function Parameters

|                                      |           |                                    |
| ------------------------------------ | --------- | ---------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to query.           |
| const char *                         | **name**  | the name of the property to query. |

## Return Value

(bool) Returns true if the property exists, or false if it doesn't.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetPropertyType](SDL_GetPropertyType)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

