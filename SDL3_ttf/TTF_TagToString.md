###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_TagToString

Convert from a 32-bit tag to a 4 character string.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_TagToString(Uint32 tag, char *string, size_t size);
```

## Function Parameters

|        |            |                                                                     |
| ------ | ---------- | ------------------------------------------------------------------- |
| Uint32 | **tag**    | the 32-bit tag to convert.                                          |
| char * | **string** | a pointer filled in with the 4 character representation of the tag. |
| size_t | **size**   | the size of the buffer pointed at by string, should be at least 4.  |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_TagToString](TTF_TagToString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

