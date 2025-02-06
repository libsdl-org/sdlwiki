###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_StringToTag

Convert from a 4 character string to a 32-bit tag.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
Uint32 TTF_StringToTag(const char *string);
```

## Function Parameters

|              |            |                                    |
| ------------ | ---------- | ---------------------------------- |
| const char * | **string** | the 4 character string to convert. |

## Return Value

(Uint32) Returns the 32-bit representation of the string.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_TagToString](TTF_TagToString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

