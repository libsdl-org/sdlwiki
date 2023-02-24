# Assertions

'''Include File(s):''' [http://hg.libsdl.org/SDL/file/default/include/SDL_assert.h SDL_assert.h]


## Introduction
This category contains functions for managing assertions.

A fairly detailed discussion of the features of SDL_assert vs the standard assert() macro, and some technical explanation about how this is implemented can be found [http://web.archive.org/web/20190322035412/https://plus.google.com/103391075724026391227/posts/KzV6sLdALX7 in this Google+ post from Ryan].

SDL_ASSERT_LEVEL affects which assertions, if any, are processed during compiling based on which function was used to create the assertion (see functions below).

SDL_ASSERT_LEVEL can be defined in your project.  If not otherwise set, SDL_ASSERT_LEVEL will default to level 2 for debug builds or level 1 for release builds.  

The following table describes each SDL_ASSERT_LEVEL setting and the corresponding impact on the three SDL_assert functions:

<table>
<tr style="background-color:#EDEDED;">
<td>'''SDL_ASSERT_LEVEL'''</td>
<td>'''Description'''</td>
<td>'''Function'''</td>
<td>'''Function Status'''</td>
<tr>
</tr>
<td><:>'''0'''</td>
<td>all assertions disabled</td>
<td>SDL_assert<br/>SDL_assert_release<br/>SDL_assert_paranoid</td>
<td>disabled<br/>disabled<br/>disabled</td>
<tr>
</tr>
<td><:>'''1'''</td>
<td>for release (default)</td>
<td>SDL_assert<br/>SDL_assert_release<br/>SDL_assert_paranoid</td>
<td>disabled<br/>'''enabled'''<br/>disabled</td>
<tr>
</tr>
<td><:>'''2'''</td>
<td>for debugging (default)</td>
<td>SDL_assert<br/>SDL_assert_release<br/>SDL_assert_paranoid</td>
<td>'''enabled'''<br/>'''enabled'''<br/>disabled</td>
<tr>
</tr>
<td><:>'''3'''</td>
<td>stringent for detailed checking</td>
<td>SDL_assert<br/>SDL_assert_release<br/>SDL_assert_paranoid</td>
<td>'''enabled'''<br/>'''enabled'''<br/>'''enabled'''</td>
</tr>
</table>


## Enumerations
<<FullSearchCached(category:CategoryEnum CategoryAssertions -title:SGEnumerations)>>

## Structures
<<FullSearchCached(category:CategoryStruct CategoryAssertions -title:SGStructures)>>

## Functions
<<FullSearchCached(category:CategoryAssertions -CategoryEnum -CategoryStruct -title:SGFunctions)>>


<!-- BEGIN CATEGORY LIST -->
* [[SDL_assert]]
* [[SDL_assert_data]]
* [[SDL_assert_paranoid]]
* [[SDL_assert_release]]
* [[SDL_AssertState]]
* [[SDL_GetAssertionHandler]]
* [[SDL_GetAssertionReport]]
* [[SDL_GetDefaultAssertionHandler]]
* [[SDL_ResetAssertionReport]]
* [[SDL_SetAssertionHandler]]
* [[SDL_TriggerBreakpoint]]
<!-- END CATEGORY LIST -->
----
CategoryCategory
