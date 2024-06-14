###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenAudioDeviceStream

Convenience function for straightforward audio init for the common case.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_AudioStream* SDL_OpenAudioDeviceStream(SDL_AudioDeviceID devid, const SDL_AudioSpec *spec, SDL_AudioStreamCallback callback, void *userdata);
```

## Function Parameters

|                                                    |              |                                                                                                                                                                                                                                                                       |
| -------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID)             | **devid**    | an audio device to open, or [SDL_AUDIO_DEVICE_DEFAULT_OUTPUT](SDL_AUDIO_DEVICE_DEFAULT_OUTPUT) or [SDL_AUDIO_DEVICE_DEFAULT_CAPTURE](SDL_AUDIO_DEVICE_DEFAULT_CAPTURE).                                                                                               |
| const [SDL_AudioSpec](SDL_AudioSpec) *             | **spec**     | the audio stream's data format. Can be NULL.                                                                                                                                                                                                                          |
| [SDL_AudioStreamCallback](SDL_AudioStreamCallback) | **callback** | a callback where the app will provide new data for playback, or receive new data for capture. Can be NULL, in which case the app will need to call [SDL_PutAudioStreamData](SDL_PutAudioStreamData) or [SDL_GetAudioStreamData](SDL_GetAudioStreamData) as necessary. |
| void *                                             | **userdata** | app-controlled pointer passed to callback. Can be NULL. Ignored if callback is NULL.                                                                                                                                                                                  |

## Return Value

([SDL_AudioStream](SDL_AudioStream) *) Returns an audio stream on success,
ready to use. NULL on error; call [SDL_GetError](SDL_GetError)() for more
information. When done with this stream, call
[SDL_DestroyAudioStream](SDL_DestroyAudioStream) to free resources and
close the device.

## Remarks

If all your app intends to do is provide a single source of PCM audio, this
function allows you to do all your audio setup in a single call.

This is also intended to be a clean means to migrate apps from SDL2.

This function will open an audio device, create a stream and bind it.
Unlike other methods of setup, the audio device will be closed when this
stream is destroyed, so the app can treat the returned
[SDL_AudioStream](SDL_AudioStream) as the only object needed to manage
audio playback.

Also unlike other functions, the audio device begins paused. This is to map
more closely to SDL2-style behavior, since there is no extra step here to
bind a stream to begin audio flowing. The audio device should be resumed
with `SDL_ResumeAudioDevice(SDL_GetAudioStreamDevice(stream));`

This function works with both playback and capture devices.

The `spec` parameter represents the app's side of the audio stream. That
is, for recording audio, this will be the output format, and for playing
audio, this will be the input format. If spec is NULL, the system will
choose the format, and the app can use
[SDL_GetAudioStreamFormat](SDL_GetAudioStreamFormat)() to obtain this
information later.

If you don't care about opening a specific audio device, you can (and
probably _should_), use
[SDL_AUDIO_DEVICE_DEFAULT_OUTPUT](SDL_AUDIO_DEVICE_DEFAULT_OUTPUT) for
playback and
[SDL_AUDIO_DEVICE_DEFAULT_CAPTURE](SDL_AUDIO_DEVICE_DEFAULT_CAPTURE) for
recording.

One can optionally provide a callback function; if NULL, the app is
expected to queue audio data for playback (or unqueue audio data if
capturing). Otherwise, the callback will begin to fire once the device is
unpaused.

Destroying the returned stream with
[SDL_DestroyAudioStream](SDL_DestroyAudioStream) will also close the audio
device associated with this stream.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAudioStreamDevice](SDL_GetAudioStreamDevice)
- [SDL_ResumeAudioDevice](SDL_ResumeAudioDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

