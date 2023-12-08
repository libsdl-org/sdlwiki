###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RWtell

Determine the current read/write offset in an [SDL_RWops](SDL_RWops.md) data stream.

## Syntax

```c
Sint64 SDL_RWtell(SDL_RWops *context);

```

## Function Parameters

|                 |                                                                                   |
| --------------- | --------------------------------------------------------------------------------- |
| **context**     | an [SDL_RWops](SDL_RWops.md) data stream object from which to get the current offset |

## Return Value

Returns the current offset in the stream, or -1 if the information can not
be determined.

## Remarks

[SDL_RWtell](SDL_RWtell.md) is actually a wrapper function that calls the
[SDL_RWops](SDL_RWops.md)'s `seek` method, with an offset of 0 bytes from
[`SDL_RW_SEEK_CUR`](SDL_RW_SEEK_CUR), to simplify application development.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
extern SDL_RWops *rw;
printf("Current position in stream: %lld\n", (long long) SDL_RWtell(rw));
if (SDL_RWseek(rw, 0, SDL_RW_SEEK_END) != -1) {
    printf("Final position in stream: %lld\n", (long long) SDL_RWtell(rw));
}
```

## Related Functions

* [SDL_RWclose](SDL_RWclose.md)
* [SDL_RWFromConstMem](SDL_RWFromConstMem.md)
* [SDL_RWFromFile](SDL_RWFromFile.md)
* [SDL_RWFromMem](SDL_RWFromMem.md)
* [SDL_RWread](SDL_RWread.md)
* [SDL_RWseek](SDL_RWseek.md)
* [SDL_RWwrite](SDL_RWwrite.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryIO](CategoryIO.md)
