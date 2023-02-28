# SDL_version

A structure that contains information about the version of SDL in use.

## Data Fields

|       |           |                             |                                 |
| ----- | --------- | --------------------------- |
| Uint8 | **major** | major version               |
| Uint8 | **minor** | minor version               |
| Uint8 | **patch** | update version (patchlevel) |

## Code Examples

```c
SDL_version compiled;
SDL_version linked;

SDL_VERSION(&compiled);
SDL_GetVersion(&linked);
SDL_Log("We compiled against SDL version %u.%u.%u ...\n",
       compiled.major, compiled.minor, compiled.patch);
SDL_Log("But we are linking against SDL version %u.%u.%u.\n",
       linked.major, linked.minor, linked.patch);
```

## Remarks

Represents the library's version as three levels:

- major revision (increments with massive changes, additions, and enhancements)
- minor revision (increments with backwards-compatible changes to the major revision), and
- patchlevel (increments with fixes to the minor revision)

The macro [SDL_VERSION](SDL_VERSION) can be used to populate this structure with information.

## Related Macros

- [SDL_COMPILEDVERSION](SDL_COMPILEDVERSION)
- [SDL_VERSION](SDL_VERSION)
- [SDL_VERSIONNUM](SDL_VERSIONNUM)
- [SDL_VERSION_ATLEAST](SDL_VERSION_ATLEAST)

## Related Functions

- [SDL_GetVersion](SDL_GetVersion)

----
[CategoryStruct](CategoryStruct), [CategoryVersion](CategoryVersion)

