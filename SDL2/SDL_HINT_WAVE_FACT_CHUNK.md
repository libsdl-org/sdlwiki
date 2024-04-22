###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WAVE_FACT_CHUNK

Controls how the fact chunk affects the loading of a WAVE file.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WAVE_FACT_CHUNK   "SDL_WAVE_FACT_CHUNK"
```

## Remarks

The fact chunk stores information about the number of samples of a WAVE
file. The Standards Update from Microsoft notes that this value can be used
to 'determine the length of the data in seconds'. This is especially useful
for compressed formats (for which this is a mandatory chunk) if they
produce multiple sample frames per block and truncating the block is not
allowed. The fact chunk can exactly specify how many sample frames there
should be in this case.

Unfortunately, most application seem to ignore the fact chunk and so SDL
ignores it by default as well.

This variable can be set to the following values:

"truncate" - Use the number of samples to truncate the wave data if the
fact chunk is present and valid "strict" - Like "truncate", but raise an
error if the fact chunk is invalid, not present for non-PCM formats, or if
the data chunk doesn't have that many samples "ignorezero" - Like
"truncate", but ignore fact chunk if the number of samples is zero "ignore"
- Ignore fact chunk entirely (default)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

