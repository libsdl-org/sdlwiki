###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenAudioDevice

Open a specific audio device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_AudioDeviceID SDL_OpenAudioDevice(SDL_AudioDeviceID devid, const SDL_AudioSpec *spec);

```

## Function Parameters

|               |                                                                                                                                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **devid**     | the device instance id to open, or [SDL_AUDIO_DEVICE_DEFAULT_OUTPUT](SDL_AUDIO_DEVICE_DEFAULT_OUTPUT) or [SDL_AUDIO_DEVICE_DEFAULT_CAPTURE](SDL_AUDIO_DEVICE_DEFAULT_CAPTURE) for the most reasonable default device. |
| **spec**      | the requested device configuration. Can be NULL to use reasonable defaults.                                                                                                                                           |

## Return Value

Returns The device ID on success, 0 on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can open both output and capture devices through this function. Output
devices will take data from bound audio streams, mix it, and send it to the
hardware. Capture devices will feed any bound audio streams with a copy of
any incoming data.

An opened audio device starts out with no audio streams bound. To start
audio playing, bind a stream and supply audio data to it. Unlike SDL2,
there is no audio callback; you only bind audio streams and make sure they
have data flowing into them (however, you can simulate SDL2's semantics
fairly closely by using
[SDL_OpenAudioDeviceStream](SDL_OpenAudioDeviceStream) instead of this
function).

If you don't care about opening a specific device, pass a `devid` of either
[`SDL_AUDIO_DEVICE_DEFAULT_OUTPUT`](SDL_AUDIO_DEVICE_DEFAULT_OUTPUT) or
[`SDL_AUDIO_DEVICE_DEFAULT_CAPTURE`](SDL_AUDIO_DEVICE_DEFAULT_CAPTURE). In
this case, SDL will try to pick the most reasonable default, and may also
switch between physical devices seamlessly later, if the most reasonable
default changes during the lifetime of this opened device (user changed the
default in the OS's system preferences, the default got unplugged so the
system jumped to a new default, the user plugged in headphones on a mobile
device, etc). Unless you have a good reason to choose a specific device,
this is probably what you want.

You may request a specific format for the audio device, but there is no
promise the device will honor that request for several reasons. As such,
it's only meant to be a hint as to what data your app will provide. Audio
streams will accept data in whatever format you specify and manage
conversion for you as appropriate.
[SDL_GetAudioDeviceFormat](SDL_GetAudioDeviceFormat) can tell you the
preferred format for the device before opening and the actual format the
device is using after opening.

It's legal to open the same device ID more than once; each successful open
will generate a new logical [SDL_AudioDeviceID](SDL_AudioDeviceID) that is
managed separately from others on the same physical device. This allows
libraries to open a device separately from the main app and bind its own
streams without conflicting.

It is also legal to open a device ID returned by a previous call to this
function; doing so just creates another logical device on the same physical
device. This may be useful for making logical groupings of audio streams.

This function returns the opened device ID on success. This is a new,
unique [SDL_AudioDeviceID](SDL_AudioDeviceID) that represents a logical
device.

Some backends might offer arbitrary devices (for example, a networked audio
protocol that can connect to an arbitrary server). For these, as a change
from SDL2, you should open a default device ID and use an SDL hint to
specify the target if you care, or otherwise let the backend figure out a
reasonable default. Most backends don't offer anything like this, and often
this would be an end user setting an environment variable for their custom
need, and not something an application should specifically manage.

When done with an audio device, possibly at the end of the app's life, one
should call [SDL_CloseAudioDevice](SDL_CloseAudioDevice)() on the returned
device id.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c

SDL_AudioSpec want;
SDL_AudioDeviceID dev;

SDL_memset(&want, 0, sizeof(want)); /* or SDL_zero(want) */
want.format = SDL_AUDIO_F32;
want.channels = 2;
want.freq = 48000;

dev = SDL_OpenAudioDevice(SDL_AUDIO_DEVICE_DEFAULT_OUTPUT, &want);
if (dev == 0) {
    SDL_Log("Failed to open audio: %s", SDL_GetError());
} else {
    SDL_ResumeAudioDevice(dev); /* start audio playing. */
    SDL_Delay(5000);  // let device play for 5 seconds
    SDL_CloseAudioDevice(dev);
}
```

## See Also

* [SDL_CloseAudioDevice](SDL_CloseAudioDevice)
* [SDL_GetAudioDeviceFormat](SDL_GetAudioDeviceFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)


