cmake_minimum_required(VERSION 3.20)
project(sdlwikipp NONE)

set(SDLWIKI_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/.." CACHE PATH "Path to sdlwiki root source folder")
set(OUTPUT_ROOT "${CMAKE_CURRENT_BINARY_DIR}/wikidir" CACHE PATH "Path to generated wiki root foler")

get_filename_component(sdlwiki_root "${SDLWIKI_ROOT}" ABSOLUTE)

message(STATUS "sdlwiki root folder is ${sdlwiki_root}")
message(STATUS "output root folder is  ${OUTPUT_ROOT}")

find_program(PANDOC_BIN NAMES pandoc)
if(NOT PANDOC_BIN)
    message(FATAL_ERROR "Cannot find pandoc")
endif()

file(GLOB_RECURSE MARKDOWN_SOURCES "${sdlwiki_root}/*.md")
file(GLOB_RECURSE MEDIAWIKI_SOURCES "${sdlwiki_root}/*.mediawiki")

list(LENGTH MARKDOWN_SOURCES  nb_markdown_sources)
list(LENGTH MEDIAWIKI_SOURCES nb_mediawiki_sources)

message(STATUS "Found ${nb_markdown_sources} Markdown pages")
message(STATUS "Found ${nb_mediawiki_sources} MediaWiki pages")

enable_testing()
foreach(src IN LISTS MARKDOWN_SOURCES MEDIAWIKI_SOURCES)
    cmake_path(RELATIVE_PATH src BASE_DIRECTORY "${sdlwiki_root}" OUTPUT_VARIABLE src_relative)
    cmake_path(GET src_relative PARENT_PATH src_reldirectory)
    if(src_reldirectory AND NOT IS_DIRECTORY "${OUTPUT_ROOT}/${src_reldirectory}")
        execute_process(
            COMMAND "${CMAKE_COMMAND}" -E make_directory "${OUTPUT_ROOT}/${src_reldirectory}"
        )
    endif()
    if(src MATCHES "\\.mediawiki$")
        set(fmt "mediawiki")
    elseif(src MATCHES "\\.md$")
        set(fmt "gfm")  # GitHub-Flavored Markdown
    else()
        message(FATAL_ERROR "Unknown document type (${src})")
    endif()
    add_test(
        NAME "${src_relative}"
        COMMAND "${PANDOC_BIN}" --fail-if-warnings --verbose -f ${fmt} -t html -o "${OUTPUT_ROOT}/${src_relative}.html" "${src}"
    )
    set_tests_properties("${src_relative}"
        PROPERTIES
            TIMEOUT 2
    )
endforeach()
