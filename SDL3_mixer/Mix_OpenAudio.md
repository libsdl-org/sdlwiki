###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_OpenAudio

Open an audio device for playback.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
int Mix_OpenAudio(SDL_AudioDeviceID devid, const SDL_AudioSpec *spec);

```

## Function Parameters

|               |                                                         |
| ------------- | ------------------------------------------------------- |
| **devid**     | the device name to open, or 0 for a reasonable default. |
| **spec**      | the audio format you'd like SDL_mixer to work in.       |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

An audio device is what generates sound, so the app must open one to make
noise.

This function will check if SDL's audio system is initialized, and if not,
it will initialize it by calling `SDL_Init(SDL_INIT_AUDIO)` on your behalf.
You are free to (and encouraged to!) initialize it yourself before calling
this function, as this gives your program more control over the process.

If you aren't particularly concerned with the specifics of the audio
device, and your data isn't in a specific format, you can pass a NULL for
the `spec` parameter and SDL_mixer will choose a reasonable default.
SDL_mixer will convert audio data you feed it to the hardware's format
behind the scenes.

That being said, if you have control of your audio data and you know its
format ahead of time, you may save CPU time by opening the audio device in
that exact format so SDL_mixer does not have to spend time converting
anything behind the scenes, and can just pass the data straight through to
the hardware.

The other reason to care about specific formats: if you plan to touch the
mix buffer directly (with [Mix_SetPostMix](Mix_SetPostMix), a registered
effect, or [Mix_HookMusic](Mix_HookMusic)), you might have code that
expects it to be in a specific format, and you should specify that here.

This function allows you to select specific audio hardware on the system
with the `devid` parameter. If you specify 0, SDL_mixer will choose the
best default it can on your behalf (which, in many cases, is exactly what
you want anyhow). This is equivalent to specifying
`SDL_AUDIO_DEVICE_DEFAULT_OUTPUT`, but is less wordy. SDL_mixer does not
offer a mechanism to determine device IDs to open, but you can use
SDL_GetAudioOutputDevices() to get a list of available devices. If you do
this, be sure to call `SDL_Init(SDL_INIT_AUDIO)` first to initialize SDL's
audio system!

If this function reports success, you are ready to start making noise! Load
some audio data and start playing!

When done with an audio device, probably at the end of the program, the app
should close the audio with [Mix_CloseAudio](Mix_CloseAudio)().

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

* [Mix_CloseAudio](Mix_CloseAudio)
* [Mix_QuerySpec](Mix_QuerySpec)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

