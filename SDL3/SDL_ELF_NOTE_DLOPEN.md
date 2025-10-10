# SDL_ELF_NOTE_DLOPEN

Note that your application has dynamic shared library dependencies.

## Header File

Defined in [<SDL3/SDL_dlopennote.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dlopennote.h)

## Syntax

```c
#define SDL_ELF_NOTE_DLOPEN(feature, description, priority, ...) \
    SDL_ELF_NOTE_INTERNAL(                                       \
        "[{\"feature\":\"" feature                               \
        "\",\"description\":\"" description                      \
        "\",\"priority\":\"" priority                            \
        "\",\"soname\":" SDL_SONAME_ARRAY(__VA_ARGS__) "}]",     \
        SDL_ELF_NOTE_UNIQUE_NAME)
```

## Remarks

You can do this by adding the following to the global scope:

```c
SDL_ELF_NOTE_DLOPEN(
    "png",
    "Support for loading PNG images using libpng (required for APNG)",
    SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED,
    "libpng12.so.0"
);
```

Or if you support multiple versions of a library, you can list them:

```c
// Our app supports SDL1, SDL2, and SDL3 by dynamically loading them
SDL_ELF_NOTE_DLOPEN(
    "SDL",
    "Create windows through SDL video backend",
    SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED
    "libSDL-1.2.so.0", "libSDL2-2.0.so.0", "libSDL3.so.0"
);
```

## Version

This macro is available since SDL 3.4.0.

## See Also

- [SDL_ELF_NOTE_DLOPEN_PRIORITY_SUGGESTED](SDL_ELF_NOTE_DLOPEN_PRIORITY_SUGGESTED)
- [SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED](SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED)
- [SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED](SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDlopenNotes](CategoryDlopenNotes)

