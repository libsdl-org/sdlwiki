# Thread Management
'''Include File(s):'''  [http://hg.libsdl.org/SDL/file/default/include/SDL_thread.h SDL_thread.h], [http://hg.libsdl.org/SDL/file/default/include/SDL_mutex.h SDL_mutex.h] (contains thread synchronization primitives)


## Introduction
This category contains functions for system independent thread management routines.

{i} ''NOTE'': You should not expect to be able to create a window, render, or receive events on any thread other than the main one.  For platform-specific exceptions or complicated options ask on the <!-- [http://lists.libsdl.org/listinfo.cgi/sdl-libsdl.org mailing list] or [http://forums.libsdl.org/viewtopic.php?t=5973 forum] --> [https://discourse.libsdl.org/ forums/mailing list].

## Enumerations
<<FullSearchCached(category:CategoryEnum CategoryThread -title:SGEnumerations)>>

<!-- #Remove this line and the ## below to use this markup if it becomes relevant to this category -->
<!-- #== Structures == -->
<!-- #<<FullSearchCached(category:CategoryStruct CategoryThread -title:SGStructures)>> -->
## Functions
<<FullSearchCached(category:CategoryThread -CategoryEnum -CategoryStruct -title:SGFunctions)>>

<!-- BEGIN CATEGORY LIST -->
- [SDL_CreateThread](SDL_CreateThread)
- [SDL_DetachThread](SDL_DetachThread)
- [SDL_GetThreadID](SDL_GetThreadID)
- [SDL_GetThreadName](SDL_GetThreadName)
- [SDL_SetThreadPriority](SDL_SetThreadPriority)
- [SDL_ThreadID](SDL_ThreadID)
- [SDL_ThreadPriority](SDL_ThreadPriority)
- [SDL_TLSCreate](SDL_TLSCreate)
- [SDL_TLSGet](SDL_TLSGet)
- [SDL_TLSSet](SDL_TLSSet)
- [SDL_WaitThread](SDL_WaitThread)
<!-- END CATEGORY LIST -->
----
[[CategoryCategory]]
