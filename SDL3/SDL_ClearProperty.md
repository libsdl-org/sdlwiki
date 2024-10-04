###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ClearProperty

Clear a property from a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
bool SDL_ClearProperty(SDL_PropertiesID props, const char *name);
```

## Function Parameters

|                                      |           |                                    |
| ------------------------------------ | --------- | ---------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to modify.          |
| const char *                         | **name**  | the name of the property to clear. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

