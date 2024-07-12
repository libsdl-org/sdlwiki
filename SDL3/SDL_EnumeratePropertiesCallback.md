###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EnumeratePropertiesCallback

A callback used to enumerate all the properties in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
typedef void (SDLCALL *SDL_EnumeratePropertiesCallback)(void *userdata, SDL_PropertiesID props, const char *name);
```

## Function Parameters

|              |                                                                    |
| ------------ | ------------------------------------------------------------------ |
| **userdata** | an app-defined pointer passed to the callback.                     |
| **props**    | the [SDL_PropertiesID](SDL_PropertiesID) that is being enumerated. |
| **name**     | the next property name in the enumeration.                         |

## Remarks

This callback is called from
[SDL_EnumerateProperties](SDL_EnumerateProperties)(), and is called once
per property in the set.

## Thread Safety

[SDL_EnumerateProperties](SDL_EnumerateProperties) holds a lock on `props`
during this callback.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_EnumerateProperties](SDL_EnumerateProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryProperties](CategoryProperties)

