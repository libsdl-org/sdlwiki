# Initialization and Shutdown
'''Include File(s):''' [http://hg.libsdl.org/SDL/file/default/include/SDL.h SDL.h]


## Introduction
The functions in this category are used to set up SDL for use and generally have global effects in your program.

=== Introduction to Initialization ===
To begin using SDL in your program [[SDL_Init]]() must be called before most other SDL functions.  The role of [[SDL_Init]]() is to properly initialize the SDL library and start each of the various subsystems requested as part of the call.

: {i} The [[CategoryIO|File I/O]] and [[CategoryThread|Threading]] subsystems are initialized by default.  To initialize other subsystems you must specifically call them.  Multiple subsystems may be OR'd together.
: ''Example:''
:: <syntaxhighlight lang="c"> SDL_Init(SDL_INIT_VIDEO|SDL_INIT_AUDIO); </syntaxhighlight>
:: This initializes the 2 default subsystems plus the [[CategoryVideo|Video]], [[CategoryAudio|Audio]], and [[CategoryEvents|Event Handling]] subsystems.
:: The [[CategoryEvents|Event Handling]] subsystem is initialized implicitly by the [[CategoryVideo|Video]] subsystem.
::

It should be noted that on some operating systems, [[SDL_Init]]() will fail if SDL_main() has not been defined as the entry point for the program.  Calling [[SDL_SetMainReady]]() prior to [[SDL_Init]]() will circumvent this failure condition, however, users should be careful when calling [[SDL_SetMainReady]]() as improper initialization may cause crashes and hard to diagnose problems.

=== Introduction to Shut Down ===
[[SDL_Quit]]() should be called before an SDL application exits to safely shut down all subsystems, including the default ones.

* It is not necessary to specify individual subsystems when using [[SDL_Quit]]() as it will automatically shut down all active subsystems.

<!-- #Remove this line and the ## in front of the following if they become relevant to this category to activate them. -->
<!-- #== Enumerations == -->
<!-- #<<FullSearchCached(category:CategoryEnum CategoryInit -title:SGEnumerations)>> -->
<!-- #== Structures == -->
<!-- #<<FullSearchCached(category:CategoryStruct CategoryInit -title:SGStructures)>> -->
## Functions
<<FullSearchCached(category:CategoryInit -CategoryEnum -CategoryStruct -title:SGFunctions)>>

<!-- BEGIN CATEGORY LIST -->
- [SDL_Init](SDL_Init)
- [SDL_InitSubSystem](SDL_InitSubSystem)
- [SDL_Quit](SDL_Quit)
- [SDL_QuitSubSystem](SDL_QuitSubSystem)
- [SDL_SetMainReady](SDL_SetMainReady)
- [SDL_WasInit](SDL_WasInit)
<!-- END CATEGORY LIST -->
----
CategoryCategory
