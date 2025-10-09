# SDL_PROP_NAME_STRING

A generic property for naming things.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
#define SDL_PROP_NAME_STRING "SDL.name"
```

## Remarks

This property is intended to be added to any
[SDL_PropertiesID](SDL_PropertiesID) that needs a generic name associated
with the property set. It is not guaranteed that any property set will
include this key, but it is convenient to have a standard key that any
piece of code could reasonably agree to use.

For example, the properties associated with an [SDL_Texture](SDL_Texture)
might have a name string of "player sprites", or an
[SDL_AudioStream](SDL_AudioStream) might have "background music", etc. This
might also be useful for an [SDL_IOStream](SDL_IOStream) to list the path
to its asset.

There is no format for the value set with this key; it is expected to be
human-readable and informational in nature, possibly for logging or
debugging purposes.

SDL does not currently set this property on any objects it creates, but
this may change in later versions; it is currently expected that apps and
external libraries will take advantage of it, when appropriate.

## Version

This macro is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryProperties](CategoryProperties)

