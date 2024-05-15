###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioSpec

The calculated values in this structure are calculated by [SDL_OpenAudio](SDL_OpenAudio)().

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
typedef struct SDL_AudioSpec
{
    int freq;                   /**< DSP frequency -- samples per second */
    SDL_AudioFormat format;     /**< Audio data format */
    Uint8 channels;             /**< Number of channels: 1 mono, 2 stereo */
    Uint8 silence;              /**< Audio buffer silence value (calculated) */
    Uint16 samples;             /**< Audio buffer size in sample FRAMES (total samples divided by channel count) */
    Uint16 padding;             /**< Necessary for some compile environments */
    Uint32 size;                /**< Audio buffer size in bytes (calculated) */
    SDL_AudioCallback callback; /**< Callback that feeds the audio device (NULL to use SDL_QueueAudio()). */
    void *userdata;             /**< Userdata passed to callback (ignored for NULL callbacks). */
} SDL_AudioSpec;
```

## Remarks

For multi-channel audio, the default SDL channel mapping is:

```
2:  FL  FR                          (stereo)
3:  FL  FR LFE                      (2.1 surround)
4:  FL  FR  BL  BR                  (quad)
5:  FL  FR LFE  BL  BR              (4.1 surround)
6:  FL  FR  FC LFE  SL  SR          (5.1 surround - last two can also be BL BR)
7:  FL  FR  FC LFE  BC  SL  SR      (6.1 surround)
8:  FL  FR  FC LFE  BL  BR  SL  SR  (7.1 surround)
```

## Code Examples

```c
SDL_AudioSpec want, have;
SDL_AudioDeviceID dev;
extern void SDLCALL MyAudioCallback(void *userdata, Uint8 *stream, int len);

SDL_memset(&want, 0, sizeof(want)); /* or SDL_zero(want) */
want.freq = 48000;
want.format = AUDIO_F32;
want.channels = 2;
want.samples = 4096;
want.callback = MyAudioCallback;  // you wrote this function elsewhere.
dev = SDL_OpenAudioDevice(NULL, 0, &want, &have, SDL_AUDIO_ALLOW_FORMAT_CHANGE);
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryAudio](CategoryAudio)

