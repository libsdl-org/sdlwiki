###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioCallback

This function is called when the audio device needs more data.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
typedef void (SDLCALL * SDL_AudioCallback) (void *userdata, Uint8 * stream, int len);
```

## Function Parameters

|              |                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------- |
| **userdata** | An application-specific parameter saved in the [SDL_AudioSpec](SDL_AudioSpec) structure. |
| **stream**   | A pointer to the audio data buffer.                                                      |
| **len**      | Length of **stream** in bytes.                                                           |

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAudio](CategoryAudio)

