###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RWtell

Determine the current read/write offset in an [SDL_RWops](SDL_RWops) data stream.

## Syntax

```c
Sint64 SDL_RWtell(SDL_RWops *context);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **context**     | a [SDL_RWops](SDL_RWops) data stream object from which to get the current offset |

## Return Value

Returns the current offset in the stream, or -1 if the information can not
be determined.

## Remarks

[SDL_RWtell](SDL_RWtell) is actually a wrapper function that calls the
[SDL_RWops](SDL_RWops)'s `seek` method, with an offset of 0 bytes from
`[SDL_RW_SEEK_CUR](SDL_RW_SEEK_CUR)`, to simplify application development.

Prior to SDL 2.0.10, this function was a macro.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
extern SDL_RWops *rw;
printf("Current position in stream: %lld\n", (long long) SDL_RWtell(rw));
if (SDL_RWseek(rw, 0, RW_SEEK_END) != -1) {
    printf("Final position in stream: %lld\n", (long long) SDL_RWtell(rw));
}
```

## Related Functions

* [SDL_RWclose](SDL_RWclose)
* [SDL_RWFromConstMem](SDL_RWFromConstMem)
* [SDL_RWFromFile](SDL_RWFromFile)
* [SDL_RWFromMem](SDL_RWFromMem)
* [SDL_RWread](SDL_RWread)
* [SDL_RWseek](SDL_RWseek)
* [SDL_RWwrite](SDL_RWwrite)

----
[CategoryAPI](CategoryAPI), [CategoryIO](CategoryIO)


