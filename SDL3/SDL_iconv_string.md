###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_iconv_string

This function converts a buffer or string between encodings in one pass, returning a string that must be freed with [SDL_free](SDL_free)() or NULL on error.

## Syntax

```c
char* SDL_iconv_string(const char *tocode,
                       const char *fromcode,
                       const char *inbuf,
                       size_t inbytesleft);

```

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

