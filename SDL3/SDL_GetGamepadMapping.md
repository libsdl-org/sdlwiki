# SDL_GetGamepadMapping

Get the current mapping of a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
char * SDL_GetGamepadMapping(SDL_Gamepad *gamepad);
```

## Function Parameters

|                              |             |                                                      |
| ---------------------------- | ----------- | ---------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | the gamepad you want to get the current mapping for. |

## Return Value

(char *) Returns a string that has the gamepad's mapping or NULL if no
mapping is available; call [SDL_GetError](SDL_GetError)() for more
information. This should be freed with [SDL_free](SDL_free)() when it is no
longer needed.

## Remarks

Details about mappings are discussed with
[SDL_AddGamepadMapping](SDL_AddGamepadMapping)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddGamepadMapping](SDL_AddGamepadMapping)
- [SDL_GetGamepadMappingForID](SDL_GetGamepadMappingForID)
- [SDL_GetGamepadMappingForGUID](SDL_GetGamepadMappingForGUID)
- [SDL_SetGamepadMapping](SDL_SetGamepadMapping)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

