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

file(GLOB_RECURSE MEDIAWIKI_SOURCES
    "${sdlwiki_root}/*.mediawiki"
)
list(LENGTH MEDIAWIKI_SOURCES nb_mediawiki_sources)

message(STATUS "Found ${nb_mediawiki_sources} mediawiki pages")

enable_testing()
foreach(src IN LISTS MEDIAWIKI_SOURCES)
    cmake_path(RELATIVE_PATH src BASE_DIRECTORY "${sdlwiki_root}" OUTPUT_VARIABLE src_relative)
    cmake_path(GET src_relative PARENT_PATH src_reldirectory)
    if(src_reldirectory AND NOT IS_DIRECTORY "${OUTPUT_ROOT}/${src_reldirectory}")
        execute_process(
            COMMAND "${CMAKE_COMMAND}" -E make_directory "${OUTPUT_ROOT}/${src_reldirectory}"
        )
    endif()
    add_test(
        NAME "${src_relative}"
        COMMAND "${PANDOC_BIN}" -f mediawiki -t html -o "${OUTPUT_ROOT}/${src_relative}.html" "${src}"
    )
    set_tests_properties("${src_relative}"
        PROPERTIES
            TIMEOUT 2
    )
endforeach()
