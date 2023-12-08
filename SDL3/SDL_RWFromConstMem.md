###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RWFromConstMem

Use this function to prepare a read-only memory buffer for use with RWops.

## Syntax

```c
SDL_RWops* SDL_RWFromConstMem(const void *mem, size_t size);

```

## Function Parameters

|              |                                                                          |
| ------------ | ------------------------------------------------------------------------ |
| **mem**      | a pointer to a read-only buffer to feed an [SDL_RWops](SDL_RWops.md) stream |
| **size**     | the buffer size, in bytes                                                |

## Return Value

Returns a pointer to a new [SDL_RWops](SDL_RWops.md) structure, or NULL if it
fails; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function sets up an [SDL_RWops](SDL_RWops.md) struct based on a memory
area of a certain size. It assumes the memory area is not writable.

Attempting to write to this RWops stream will report an error without
writing to the memory buffer.

This memory buffer is not copied by the RWops; the pointer you provide must
remain valid until you close the stream. Closing the stream will not free
the original buffer.

If you need to write to a memory buffer, you should use
[SDL_RWFromMem](SDL_RWFromMem.md)() with a writable buffer of memory instead.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
char bitmap[] = {
    66, 77, 86, 2, 0, 0, 0, 0 ...
};
SDL_RWops *rw = SDL_RWFromConstMem(bitmap, sizeof(bitmap));
SDL_Surface *img = SDL_LoadBMP_RW(rw, 1); /* Automatically frees the RWops struct for us */
/* Do something with img... */
```

## Related Functions

* [SDL_RWclose](SDL_RWclose.md)
* [SDL_RWFromConstMem](SDL_RWFromConstMem.md)
* [SDL_RWFromFile](SDL_RWFromFile.md)
* [SDL_RWFromMem](SDL_RWFromMem.md)
* [SDL_RWread](SDL_RWread.md)
* [SDL_RWseek](SDL_RWseek.md)
* [SDL_RWtell](SDL_RWtell.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryIO](CategoryIO.md)
