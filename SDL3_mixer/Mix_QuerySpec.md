###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_QuerySpec

Find out what the actual audio device parameters are.

## Syntax

```c
int Mix_QuerySpec(int *frequency, Uint16 *format, int *channels);

```

## Function Parameters

|                   |                                                                    |
| ----------------- | ------------------------------------------------------------------ |
| **frequency**     | On return, will be filled with the audio device's frequency in Hz. |
| **format**        | On return, will be filled with the audio device's format.          |
| **channels**      | On return, will be filled with the audio device's channel count.   |

## Return Value

Returns 1 if the audio device has been opened, 0 otherwise.

## Remarks

Note this is only important if the app intends to touch the audio buffers
being sent to the hardware directly. If an app just wants to play audio
files and let SDL_mixer handle the low-level details, this function can
probably be ignored.

If the audio device is not opened, this function will return 0.

## Version

This function is available since SDL_mixer 3.0.0.

## Related Functions

* [Mix_OpenAudio](Mix_OpenAudio)

----
[CategoryAPI](CategoryAPI)

