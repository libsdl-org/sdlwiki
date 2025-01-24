# SDL_crc32

Calculate a CRC-32 value.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
Uint32 SDL_crc32(Uint32 crc, const void *data, size_t len);
```

## Function Parameters

|                  |          |                                                                  |
| ---------------- | -------- | ---------------------------------------------------------------- |
| [Uint32](Uint32) | **crc**  | the current checksum for this data set, or 0 for a new data set. |
| const void *     | **data** | a new block of data to add to the checksum.                      |
| size_t           | **len**  | the size, in bytes, of the new block of data.                    |

## Return Value

([Uint32](Uint32)) Returns a CRC-32 checksum value of all blocks in the
data set.

## Remarks

https://en.wikipedia.org/wiki/Cyclic_redundancy_check

This function can be called multiple times, to stream data to be
checksummed in blocks. Each call must provide the previous CRC-32 return
value to be updated with the next block. The first call to this function
for a set of blocks should pass in a zero CRC value.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

