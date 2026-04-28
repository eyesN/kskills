



---
name: kskills
description: Provides a set of tools for a custom coding agent, mimicking the capabilities of the Claw Code harness.
---

# kskills

## Overview

This skill provides a bridge to a custom Python script that implements a set of agentic tools for coding. The tools are defined in `scripts/gemini_agent_tools.py`.

## Usage

To use the tools provided by this skill, you need to execute the `gemini_agent_tools.py` script with the appropriate command and arguments. The script is designed to be called from the command line using the `run_shell_command` tool.

The general syntax is:
`python kskills/scripts/gemini_agent_tools.py <command> [arguments]`

### Available Commands

Here are the available commands and their arguments:

**File System**
*   `read_file --file_path <path>`: Reads the contents of a file.
*   `write_file --file_path <path> --content <string>`: Writes content to a file.
*   `edit_file --file_path <path> --search_string <string> --replace_string <string>`: Edits a file.
*   `list_directory --directory_path <path> [--pattern <glob>]`: Lists files in a directory.

**Search & Discovery**
*   `grep_search --regex_pattern <pattern> --directory_path <path>`: Searches for a regex pattern in a directory.
*   `web_search --query <query>`: Searches the web.
*   `web_fetch --url <url>`: Fetches content from a URL.
*   `tool_search`: Lists available tools.

**Execution**
*   `bash_execute --command <command> [--background]`: Executes a bash command.

**LSP**
*   `lsp_query --query_type <type> --file_path <path> [--line_number <int>]`: Queries the LSP.

**Task & Multi-Agent Planning**
*   `task_registry --action <action> [--task_id <id>] [--task_details <string>]`: Manages tasks.
*   `spawn_subagent --objective <string> [--working_directory <path>]`: Spawns a sub-agent.
*   `scratchpad_edit --content <string>`: Edits the scratchpad.

## Example

To read the file `/Users/adityanegi/Documents/libsignal/README.md`, you would use the following command:

`python kskills/scripts/gemini_agent_tools.py read_file --file_path /Users/adityanegi/Documents/libsignal/README.md`

## Next Steps

The basic argument parsing logic has been added to the script. The next step is to implement the actual logic for the execution and planning tools which are currently just stubs (e.g., `bash_execute`, `lsp_query`, `task_registry`, `spawn_subagent`, `scratchpad_edit`).
