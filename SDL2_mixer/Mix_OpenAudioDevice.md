###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_OpenAudioDevice

Open a specific audio device for playback.

## Syntax

```c
int Mix_OpenAudioDevice(int frequency, Uint16 format, int channels, int chunksize, const char* device, int allowed_changes);

```

## Function Parameters

|                         |                                                                              |
| ----------------------- | ---------------------------------------------------------------------------- |
| **frequency**           | the frequency to playback audio at (in Hz).                                  |
| **format**              | audio format, one of SDL's AUDIO_* values.                                   |
| **channels**            | number of channels (1 is mono, 2 is stereo, etc).                            |
| **chunksize**           | audio buffer size in sample FRAMES (total samples divided by channel count). |
| **device**              | the device name to open, or NULL to choose a reasonable default.             |
| **allowed_changes**     | Allow change flags (see SDL_AUDIO_ALLOW_* flags)                             |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

(A slightly simpler version of this function is available in
[Mix_OpenAudio](Mix_OpenAudio)(), which still might meet most applications'
needs.)

An audio device is what generates sound, so the app must open one to make
noise.

This function will check if SDL's audio system is initialized, and if not,
it will initialize it by calling `SDL_Init(SDL_INIT_AUDIO)` on your behalf.
You are free to (and encouraged to!) initialize it yourself before calling
this function, as this gives your program more control over the process.

If you aren't particularly concerned with the specifics of the audio
device, and your data isn't in a specific format, the values you use here
can just be reasonable defaults. SDL_mixer will convert audio data you feed
it to the correct format on demand.

That being said, if you have control of your audio data and you know its
format ahead of time, you can save CPU time by opening the audio device in
that exact format so SDL_mixer does not have to spend time converting
anything behind the scenes, and can just pass the data straight through to
the hardware. On some platforms, where the hardware only supports specific
settings, you might have to be careful to make everything match, but your
own data is often easier to control, so aim to open the device for what you
need.

The other reason to care about specific formats: if you plan to touch the
mix buffer directly (with [Mix_SetPostMix](Mix_SetPostMix), a registered
effect, or [Mix_HookMusic](Mix_HookMusic)), you might have code that
expects it to be in a specific format, and you should specify that here.

The audio device frequency is specified in Hz; in modern times, 48000 is
often a reasonable default.

The audio device format is one of SDL's AUDIO_* constants. AUDIO_S16SYS
(16-bit audio) is probably a safe default. More modern systems may prefer
AUDIO_F32SYS (32-bit floating point audio).

The audio device channels are generally 1 for mono output, or 2 for stereo,
but the brave can try surround sound configs with 4 (quad), 6 (5.1), 7
(6.1) or 8 (7.1).

The audio device's chunk size is the number of sample frames (one sample
per frame for mono output, two samples per frame in a stereo setup, etc)
that are fed to the device at once. The lower the number, the lower the
latency, but you risk dropouts if it gets too low. 2048 is often a
reasonable default, but your app might want to experiment with 1024 or
4096.

You may only have one audio device open at a time; if you want to change a
setting, you must close the device and reopen it, which is not something
you can do seamlessly during playback.

This function allows you to select specific audio hardware on the system
with the `device` parameter. If you specify NULL, SDL_mixer will choose the
best default it can on your behalf (which, in many cases, is exactly what
you want anyhow). SDL_mixer does not offer a mechanism to determine device
names to open, but you can use SDL_GetNumAudioDevices() to get a count of
available devices and then SDL_GetAudioDeviceName() in a loop to obtain a
list. If you do this, be sure to call `SDL_Init(SDL_INIT_AUDIO)` first to
initialize SDL's audio system!

The `allowed_changes` parameter specifies what settings are flexible. These
are the `SDL_AUDIO_ALLOW_*` flags from SDL. These tell SDL_mixer that the
app doesn't mind if a specific setting changes. For example, the app might
need stereo data in Sint16 format, but if the sample rate or chunk size
changes, the app can handle that. In that case, the app would specify
`SDL_AUDIO_ALLOW_FORMAT_CHANGE|SDL_AUDIO_ALLOW_SAMPLES_CHANGE`. In this
case, if the system's hardware requires something other than the requested
format, SDL_mixer can select what the hardware demands instead of the app.
If the `SDL_AUDIO_ALLOW_` flag is not specified, SDL_mixer must convert
data behind the scenes between what the app demands and what the hardware
requires. If your app needs precisely what is requested, specify zero for
`allowed_changes`.

If changes were allowed, the app can use [Mix_QuerySpec](Mix_QuerySpec)()
to determine the final device settings.

If this function reports success, you are ready to start making noise! Load
some audio data and start playing!

When done with an audio device, probably at the end of the program, the app
should dispose of the device with [Mix_CloseAudio](Mix_CloseAudio)().

## Version

This function is available since SDL_mixer 2.0.2.

## Related Functions

* [Mix_OpenAudio](Mix_OpenAudio)
* [Mix_CloseAudio](Mix_CloseAudio)
* [Mix_QuerySpec](Mix_QuerySpec)

----
[CategoryAPI](CategoryAPI)

