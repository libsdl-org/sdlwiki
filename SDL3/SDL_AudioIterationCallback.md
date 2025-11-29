# SDL_AudioIterationCallback

A callback that fires around an audio device's processing work.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
typedef void (SDLCALL *SDL_AudioIterationCallback)(void *userdata, SDL_AudioDeviceID devid, bool start);
```

## Function Parameters

|              |                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| **userdata** | a pointer provided by the app through [SDL_SetAudioIterationCallbacks](SDL_SetAudioIterationCallbacks), for its own use. |
| **devid**    | the audio device this callback is running for.                                                                     |
| **start**    | true if this is the start of the iteration, false if the end.                                                      |

## Remarks

This callback fires when a logical audio device is about to start accessing
its bound audio streams, and fires again when it has finished accessing
them. It covers the range of one "iteration" of the audio device.

It can be useful to use this callback to update state that must apply to
all bound audio streams atomically: to make sure state changes don't happen
while half of the streams are already processed for the latest audio
buffer.

This callback should run as quickly as possible and not block for any
significant time, as this callback delays submission of data to the audio
device, which can cause audio playback problems. This callback delays all
audio processing across a single physical audio device: all its logical
devices and all bound audio streams. Use it carefully.

## Thread Safety

This will run from a background thread owned by SDL. The application is
responsible for locking resources the callback touches that need to be
protected.

## Version

This datatype is available since SDL 3.4.0.

## See Also

- [SDL_SetAudioIterationCallbacks](SDL_SetAudioIterationCallbacks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAudio](CategoryAudio)

