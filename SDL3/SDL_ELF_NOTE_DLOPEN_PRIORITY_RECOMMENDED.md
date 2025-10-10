# SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED

Use this macro with [SDL_ELF_NOTE_DLOPEN](SDL_ELF_NOTE_DLOPEN)() to note that a dynamic shared library dependency is recommended.

## Header File

Defined in [<SDL3/SDL_dlopennote.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dlopennote.h)

## Syntax

```c
#define SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED "recommended"
```

## Remarks

Important functionality needs the dependency, the binary will work but in
most cases the dependency should be provided.

## Version

This macro is available since SDL 3.4.0.

## See Also

- [SDL_ELF_NOTE_DLOPEN](SDL_ELF_NOTE_DLOPEN)
- [SDL_ELF_NOTE_DLOPEN_PRIORITY_SUGGESTED](SDL_ELF_NOTE_DLOPEN_PRIORITY_SUGGESTED)
- [SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED](SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDlopenNotes](CategoryDlopenNotes)

