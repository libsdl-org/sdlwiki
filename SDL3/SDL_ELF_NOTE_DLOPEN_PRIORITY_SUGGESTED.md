# SDL_ELF_NOTE_DLOPEN_PRIORITY_SUGGESTED

Use this macro with [SDL_ELF_NOTE_DLOPEN](SDL_ELF_NOTE_DLOPEN)() to note that a dynamic shared library dependency is optional.

## Header File

Defined in [<SDL3/SDL_dlopennote.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dlopennote.h)

## Syntax

```c
#define SDL_ELF_NOTE_DLOPEN_PRIORITY_SUGGESTED   "suggested"
```

## Remarks

Optional functionality uses the dependency, the binary will work and the
dependency is only needed for full-featured installations.

## Version

This macro is available since SDL 3.4.0.

## See Also

- [SDL_ELF_NOTE_DLOPEN](SDL_ELF_NOTE_DLOPEN)
- [SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED](SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED)
- [SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED](SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDlopenNotes](CategoryDlopenNotes)

