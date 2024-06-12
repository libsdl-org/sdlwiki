###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LoadFile_RW

Load all the data from an SDL data stream.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
void* SDL_LoadFile_RW(SDL_RWops *src,
                  size_t *datasize,
                  int freesrc);
```

## Function Parameters

|                          |              |                                                                           |
| ------------------------ | ------------ | ------------------------------------------------------------------------- |
| [SDL_RWops](SDL_RWops) * | **src**      | the [SDL_RWops](SDL_RWops) to read all available data from                |
| size_t *                 | **datasize** | if not NULL, will store the number of bytes read                          |
| int                      | **freesrc**  | if non-zero, calls [SDL_RWclose](SDL_RWclose)() on `src` before returning |

## Return Value

(void *) Returns the data, or NULL if there was an error.

## Remarks

The data is allocated with a zero byte at the end (null terminated) for
convenience. This extra byte is not included in the value reported via
`datasize`.

The data should be freed with [SDL_free](SDL_free)().

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRWOPS](CategoryRWOPS)

