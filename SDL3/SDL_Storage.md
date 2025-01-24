# SDL_Storage

An abstract interface for filesystem access.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
typedef struct SDL_Storage SDL_Storage;
```

## Remarks

This is an opaque datatype. One can create this object using standard SDL
functions like [SDL_OpenTitleStorage](SDL_OpenTitleStorage) or
[SDL_OpenUserStorage](SDL_OpenUserStorage), etc, or create an object with a
custom implementation using [SDL_OpenStorage](SDL_OpenStorage).

## Version

This struct is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStorage](CategoryStorage)

