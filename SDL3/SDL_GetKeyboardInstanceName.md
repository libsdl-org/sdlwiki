###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetKeyboardInstanceName

Get the name of a keyboard.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
const char* SDL_GetKeyboardInstanceName(SDL_KeyboardID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the keyboard instance ID |

## Return Value

Returns the name of the selected keyboard, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function returns "" if the keyboard doesn't have a name.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetKeyboards](SDL_GetKeyboards)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

