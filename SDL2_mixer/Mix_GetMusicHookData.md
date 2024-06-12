###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicHookData

Get a pointer to the user data for the current music hook.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
void * Mix_GetMusicHookData(void);
```

## Return Value

(void *) Returns pointer to the user data previously passed to
[Mix_HookMusic](Mix_HookMusic).

## Remarks

This returns the `arg` pointer last passed to
[Mix_HookMusic](Mix_HookMusic)(), or NULL if that function has never been
called.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

