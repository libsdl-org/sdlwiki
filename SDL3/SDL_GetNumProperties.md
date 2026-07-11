# SDL_GetNumProperties

Get the current number of items in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
int SDL_GetNumProperties(SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                          |
| ------------------------------------ | --------- | ------------------------ |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to query. |

## Return Value

(int) Returns the number of property items available.

## Remarks

For an invalid [SDL_PropertiesID](SDL_PropertiesID), this returns zero and
does not set an error message.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

