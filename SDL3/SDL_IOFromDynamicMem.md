###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IOFromDynamicMem

Use this function to create an [SDL_IOStream](SDL_IOStream) that is backed by dynamically allocated memory.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
SDL_IOStream* SDL_IOFromDynamicMem(void);
```

## Return Value

Returns a pointer to a new [SDL_IOStream](SDL_IOStream) structure, or NULL
if it fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This supports the following properties to provide access to the memory and
control over allocations:

- [`SDL_PROP_IOSTREAM_DYNAMIC_MEMORY_POINTER`](SDL_PROP_IOSTREAM_DYNAMIC_MEMORY_POINTER):
  a pointer to the internal memory of the stream. This can be set to NULL
  to transfer ownership of the memory to the application, which should free
  the memory with [SDL_free](SDL_free)(). If this is done, the next
  operation on the stream must be [SDL_CloseIO](SDL_CloseIO)().
- [`SDL_PROP_IOSTREAM_DYNAMIC_CHUNKSIZE_NUMBER`](SDL_PROP_IOSTREAM_DYNAMIC_CHUNKSIZE_NUMBER):
  memory will be allocated in multiples of this size, defaulting to 1024.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CloseIO](SDL_CloseIO)
- [SDL_ReadIO](SDL_ReadIO)
- [SDL_SeekIO](SDL_SeekIO)
- [SDL_TellIO](SDL_TellIO)
- [SDL_WriteIO](SDL_WriteIO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

