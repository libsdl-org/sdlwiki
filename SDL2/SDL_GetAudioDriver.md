###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetAudioDriver

Use this function to get the name of a built in audio driver.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
const char* SDL_GetAudioDriver(int index);
```

## Function Parameters

|     |           |                                                                                                                  |
| --- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| int | **index** | the index of the audio driver; the value ranges from 0 to [SDL_GetNumAudioDrivers](SDL_GetNumAudioDrivers)() - 1 |

## Return Value

(const char *) Returns the name of the audio driver at the requested index,
or NULL if an invalid index was specified.

## Remarks

The list of audio drivers is given in the order that they are normally
initialized by default; the drivers that seem more reasonable to choose
first (as far as the SDL developers believe) are earlier in the list.

The names of drivers are all simple, low-ASCII identifiers, like "alsa",
"coreaudio" or "xaudio2". These never have Unicode characters, and are not
meant to be proper names.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetNumAudioDrivers](SDL_GetNumAudioDrivers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

