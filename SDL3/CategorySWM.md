# Platform-specific Window Management

'''Include File(s):'''  [http://hg.libsdl.org/SDL/file/default/include/SDL_syswm.h SDL_syswm.h]


## Introduction
This category contains functions for handling advanced, platform-specific window management tasks.

Your application has access to a special type of event, [[SDL_SysWMEvent|SDL_EVENT_SYSWM]], which uses the [[SDL_SysWMmsg]] structure and contains window-manager specific information.  This arrives whenever an unhandled window event occurs.  This event is ignored by default, but you can enable it with [[SDL_EventState]]().

## Enumerations

<!-- BEGIN CATEGORY LIST -->
- [SDL_GetWindowWMInfo](SDL_GetWindowWMInfo)
- [SDL_SYSWM_TYPE](SDL_SYSWM_TYPE)
- [SDL_SysWMinfo](SDL_SysWMinfo)
- [SDL_SysWMmsg](SDL_SysWMmsg)
<!-- END CATEGORY LIST -->

## Structures


## Functions


----
[CategoryCategory](CategoryCategory)
