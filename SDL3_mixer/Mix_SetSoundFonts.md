###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetSoundFonts

Set SoundFonts paths to use by supported MIDI backends.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool Mix_SetSoundFonts(const char *paths);
```

## Function Parameters

|              |           |                                                                                  |
| ------------ | --------- | -------------------------------------------------------------------------------- |
| const char * | **paths** | Paths on the filesystem where SoundFonts are available, separated by semicolons. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

You may specify multiple paths in a single string by separating them with
semicolons; they will be searched in the order listed.

This function replaces any previously-specified paths.

Passing a NULL path will remove any previously-specified paths.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

