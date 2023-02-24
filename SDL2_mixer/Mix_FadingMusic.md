###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_FadingMusic

Query the fading status of the music stream.

## Syntax

```c
Mix_Fading Mix_FadingMusic(void);

```

## Return Value

Returns the current fading status of the music stream.

## Remarks

This reports one of three values:

- `[MIX_NO_FADING](MIX_NO_FADING)`
- `[MIX_FADING_OUT](MIX_FADING_OUT)`
- `[MIX_FADING_IN](MIX_FADING_IN)`

If music is not currently playing, this returns
`[MIX_NO_FADING](MIX_NO_FADING)`.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

