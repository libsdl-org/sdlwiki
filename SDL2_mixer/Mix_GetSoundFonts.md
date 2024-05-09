###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetSoundFonts

Get SoundFonts paths to use by supported MIDI backends.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
const char* Mix_GetSoundFonts(void);

```

## Return Value

Returns semicolon-separated list of sound font paths.

## Remarks

There are several factors that determine what will be reported by this
function:

- If the boolean _SDL hint_ `"SDL_FORCE_SOUNDFONTS"` is set, AND the
  `"SDL_SOUNDFONTS"` _environment variable_ is also set, this function will
  return that environment variable regardless of whether
  [Mix_SetSoundFounts](Mix_SetSoundFounts)() was ever called.
- Otherwise, if [Mix_SetSoundFonts](Mix_SetSoundFonts)() was successfully
  called with a non-NULL path, this function will return the string passed
  to that function.
- Otherwise, if the `"SDL_SOUNDFONTS"` variable is set, this function will
  return that environment variable.
- Otherwise, this function will search some common locations on the
  filesystem, and if it finds a SoundFont there, it will return that.
- Failing everything else, this function returns NULL.

This returns a pointer to internal (possibly read-only) memory, and it
should not be modified or free'd by the caller.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

