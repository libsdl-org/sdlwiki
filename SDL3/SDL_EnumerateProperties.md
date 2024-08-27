###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EnumerateProperties

Enumerate the properties contained in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
SDL_bool SDL_EnumerateProperties(SDL_PropertiesID props, SDL_EnumeratePropertiesCallback callback, void *userdata);
```

## Function Parameters

|                                                                    |              |                                         |
| ------------------------------------------------------------------ | ------------ | --------------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID)                               | **props**    | the properties to query.                |
| [SDL_EnumeratePropertiesCallback](SDL_EnumeratePropertiesCallback) | **callback** | the function to call for each property. |
| void *                                                             | **userdata** | a pointer that is passed to `callback`. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

The callback function is called for each property in the group of
properties. The properties are locked during enumeration.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

