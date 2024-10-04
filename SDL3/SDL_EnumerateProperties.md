###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_EnumerateProperties

Enumerate the properties contained in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
bool SDL_EnumerateProperties(SDL_PropertiesID props, SDL_EnumeratePropertiesCallback callback, void *userdata);
```

## Function Parameters

|                                                                    |              |                                         |
| ------------------------------------------------------------------ | ------------ | --------------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID)                               | **props**    | the properties to query.                |
| [SDL_EnumeratePropertiesCallback](SDL_EnumeratePropertiesCallback) | **callback** | the function to call for each property. |
| void *                                                             | **userdata** | a pointer that is passed to `callback`. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The callback function is called for each property in the group of
properties. The properties are locked during enumeration.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

