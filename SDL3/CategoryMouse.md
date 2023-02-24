
# Mouse Support

'''Include File(s):'''  [http://hg.libsdl.org/SDL/file/default/include/SDL_mouse.h SDL_mouse.h]

<!-- <span color="green">Alternate Include File:  [http://hg.libsdl.org/SDL/file/default/include/SDL_input.h SDL_input.h]</span> -->


## Introduction

This category contains functions for handling inputs from mice and other similar pointing devices, as well as some cursor management tasks.

Please note that this ONLY discusses "mice" with the notion of the desktop GUI. You (usually) have one system cursor, and the OS hides the hardware details from you. If you plug in 10 mice, all ten move that one cursor. For many applications and games this is perfect, and this API has served hundreds of SDL programs well since its birth.

<!-- #It's not the whole picture, though. If you want more lowlevel control, SDL offers a different API that gives you visibility into each input device, multi-touch interfaces, etc.  -->

<!-- #The other API is in [http://hg.libsdl.org/SDL/file/100f7ab48946/include/SDL_input.h SDL_input.h].  See [[CategoryInput|Input Device Support]] for more.   -->

<!-- #Those two APIs are incompatible, and you usually should not use both at the same time. But for legacy purposes, this API refers to a "mouse" when it actually means the system pointer and not a physical mouse. -->


<!-- #Remove this line and the ## below to use this markup if it becomes relevant to this category -->
<!-- #== Enumerations == -->
<!-- #<<FullSearchCached(category:CategoryEnum CategoryMouse -title:SGEnumerations)>> -->

<!-- #== Structures == -->
<!-- #<<FullSearchCached(category:CategoryStruct CategoryMouse -title:SGStructures)>> -->

## Functions
<<FullSearchCached(category:CategoryMouse -CategoryEnum -CategoryStruct -title:SGFunctions)>>

<!-- BEGIN CATEGORY LIST -->
- [SDL_CaptureMouse](SDL_CaptureMouse)
- [SDL_CreateColorCursor](SDL_CreateColorCursor)
- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_CreateSystemCursor](SDL_CreateSystemCursor)
- [SDL_GetCursor](SDL_GetCursor)
- [SDL_GetDefaultCursor](SDL_GetDefaultCursor)
- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)
- [SDL_GetMouseFocus](SDL_GetMouseFocus)
- [SDL_GetMouseState](SDL_GetMouseState)
- [SDL_GetRelativeMouseMode](SDL_GetRelativeMouseMode)
- [SDL_GetRelativeMouseState](SDL_GetRelativeMouseState)
- [SDL_SetCursor](SDL_SetCursor)
- [SDL_SetRelativeMouseMode](SDL_SetRelativeMouseMode)
- [SDL_ShowCursor](SDL_ShowCursor)
- [SDL_WarpMouseGlobal](SDL_WarpMouseGlobal)
- [SDL_WarpMouseInWindow](SDL_WarpMouseInWindow)
<!-- END CATEGORY LIST -->
----
CategoryCategory
