###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClearProperty

Clear a property from a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
int SDL_ClearProperty(SDL_PropertiesID props, const char *name);
```

## Function Parameters

|                                      |           |                                    |
| ------------------------------------ | --------- | ---------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to modify.          |
| const char *                         | **name**  | the name of the property to clear. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

