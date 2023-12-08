###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicHookData

Get a pointer to the user data for the current music hook.

## Syntax

```c
void * Mix_GetMusicHookData(void);

```

## Return Value

Returns pointer to the user data previously passed to
[Mix_HookMusic](Mix_HookMusic.md).

## Remarks

This returns the `arg` pointer last passed to
[Mix_HookMusic](Mix_HookMusic.md)(), or NULL if that function has never been
called.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
