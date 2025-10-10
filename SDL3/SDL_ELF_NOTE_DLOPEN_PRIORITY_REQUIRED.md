# SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED

Use this macro with [SDL_ELF_NOTE_DLOPEN](SDL_ELF_NOTE_DLOPEN)() to note that a dynamic shared library dependency is required.

## Header File

Defined in [<SDL3/SDL_dlopennote.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dlopennote.h)

## Syntax

```c
#define SDL_ELF_NOTE_DLOPEN_PRIORITY_REQUIRED    "required"
```

## Remarks

Core functionality needs the dependency, the binary will not work if it
cannot be found.

## Version

This macro is available since SDL 3.4.0.

## See Also

- [SDL_ELF_NOTE_DLOPEN](SDL_ELF_NOTE_DLOPEN)
- [SDL_ELF_NOTE_DLOPEN_PRIORITY_SUGGESTED](SDL_ELF_NOTE_DLOPEN_PRIORITY_SUGGESTED)
- [SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED](SDL_ELF_NOTE_DLOPEN_PRIORITY_RECOMMENDED)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDlopenNotes](CategoryDlopenNotes)

