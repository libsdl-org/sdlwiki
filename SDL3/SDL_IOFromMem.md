# SDL_IOFromMem

Use this function to prepare a read-write memory buffer for use with [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
SDL_IOStream * SDL_IOFromMem(void *mem, size_t size);
```

## Function Parameters

|        |          |                                                                       |
| ------ | -------- | --------------------------------------------------------------------- |
| void * | **mem**  | a pointer to a buffer to feed an [SDL_IOStream](SDL_IOStream) stream. |
| size_t | **size** | the buffer size, in bytes.                                            |

## Return Value

([SDL_IOStream](SDL_IOStream) *) Returns a pointer to a new
[SDL_IOStream](SDL_IOStream) structure or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function sets up an [SDL_IOStream](SDL_IOStream) struct based on a
memory area of a certain size, for both read and write access.

This memory buffer is not copied by the [SDL_IOStream](SDL_IOStream); the
pointer you provide must remain valid until you close the stream.

If you need to make sure the [SDL_IOStream](SDL_IOStream) never writes to
the memory buffer, you should use
[SDL_IOFromConstMem](SDL_IOFromConstMem)() with a read-only buffer of
memory instead.

The following properties will be set at creation time by SDL:

- [`SDL_PROP_IOSTREAM_MEMORY_POINTER`](SDL_PROP_IOSTREAM_MEMORY_POINTER):
  this will be the `mem` parameter that was passed to this function.
- [`SDL_PROP_IOSTREAM_MEMORY_SIZE_NUMBER`](SDL_PROP_IOSTREAM_MEMORY_SIZE_NUMBER):
  this will be the `size` parameter that was passed to this function.

Additionally, the following properties are recognized:

- [`SDL_PROP_IOSTREAM_MEMORY_FREE_FUNC_POINTER`](SDL_PROP_IOSTREAM_MEMORY_FREE_FUNC_POINTER):
  if this property is set to a non-NULL value it will be interpreted as a
  function of [SDL_free_func](SDL_free_func) type and called with the
  passed `mem` pointer when closing the stream. By default it is unset,
  i.e., the memory will not be freed.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_IOFromConstMem](SDL_IOFromConstMem)
- [SDL_CloseIO](SDL_CloseIO)
- [SDL_FlushIO](SDL_FlushIO)
- [SDL_ReadIO](SDL_ReadIO)
- [SDL_SeekIO](SDL_SeekIO)
- [SDL_TellIO](SDL_TellIO)
- [SDL_WriteIO](SDL_WriteIO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

