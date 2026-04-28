"""
gemini_agent_tools.py

This module contains the function declarations (schemas) for a Gemini-based 
coding agent, mimicking the capabilities of the Claw Code harness. 

You can pass the `AGENT_TOOLS` list directly to the `tools` parameter 
in the google-generativeai SDK.
"""

# 1. File System & Editing Tools
read_file = {
    "name": "read_file",
    "description": "Reads the contents of a specific file.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "file_path": {
                "type": "STRING",
                "description": "The absolute or relative path to the file."
            }
        },
        "required": ["file_path"]
    }
}

write_file = {
    "name": "write_file",
    "description": "Creates a new file or completely overwrites an existing one.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "file_path": {
                "type": "STRING",
                "description": "The path where the file should be written."
            },
            "content": {
                "type": "STRING",
                "description": "The full content to write to the file."
            }
        },
        "required": ["file_path", "content"]
    }
}

edit_file = {
    "name": "edit_file",
    "description": "Performs targeted find-and-replace edits within an existing file.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "file_path": {
                "type": "STRING",
                "description": "The path to the file."
            },
            "search_string": {
                "type": "STRING",
                "description": "The exact string or regex pattern to find."
            },
            "replace_string": {
                "type": "STRING",
                "description": "The exact string to replace it with."
            }
        },
        "required": ["file_path", "search_string", "replace_string"]
    }
}

list_directory = {
    "name": "list_directory",
    "description": "Lists files in a directory or searches for files matching a glob pattern.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "directory_path": {
                "type": "STRING",
                "description": "The directory to search."
            },
            "pattern": {
                "type": "STRING",
                "description": "Optional glob pattern (e.g., **/*.py)."
            }
        },
        "required": ["directory_path"]
    }
}

# 2. Search & Discovery Tools
grep_search = {
    "name": "grep_search",
    "description": "Runs a regex search across the codebase.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "regex_pattern": {
                "type": "STRING",
                "description": "The regular expression to search for."
            },
            "directory_path": {
                "type": "STRING",
                "description": "The root directory to start the search from."
            }
        },
        "required": ["regex_pattern", "directory_path"]
    }
}

web_search = {
    "name": "web_search",
    "description": "Searches the internet for documentation or information.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "query": {
                "type": "STRING",
                "description": "The search query."
            },
            "num_results": {
                "type": "INTEGER",
                "description": "The number of results to return."
            }
        },
        "required": ["query"]
    }
}

web_fetch = {
    "name": "web_fetch",
    "description": "Fetches the raw content of a specific URL.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "url": {
                "type": "STRING",
                "description": "The full URL to fetch."
            }
        },
        "required": ["url"]
    }
}

tool_search = {
    "name": "tool_search",
    "description": "Discovers custom scripts or environmental tools available to the agent.",
    "parameters": {
        "type": "OBJECT",
        "properties": {}, # No parameters needed to list tools
        "required": []
    }
}

# 3. Execution Tools
bash_execute = {
    "name": "bash_execute",
    "description": "Executes a bash/terminal command in the current environment.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "command": {
                "type": "STRING",
                "description": "The bash command to run."
            },
            "background": {
                "type": "BOOLEAN",
                "description": "Set to true if the command should run asynchronously (e.g., starting a server)."
            }
        },
        "required": ["command"]
    }
}

# 4. Language Server Protocol (LSP) Tools
lsp_query = {
    "name": "lsp_query",
    "description": "Queries the local compiler/LSP for symbols, definitions, references, or diagnostics.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "query_type": {
                "type": "STRING",
                "description": "The type of LSP query: 'symbols', 'references', 'diagnostics', 'definition', or 'hover'."
            },
            "file_path": {
                "type": "STRING",
                "description": "The path to the file to analyze."
            },
            "line_number": {
                "type": "INTEGER",
                "description": "Optional: Specific line number for hover or definition."
            }
        },
        "required": ["query_type", "file_path"]
    }
}

# 5. Task & Multi-Agent Planning
task_registry = {
    "name": "task_registry",
    "description": "Creates, gets, lists, updates, or stops sub-tasks in the agent's task registry.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "action": {
                "type": "STRING",
                "description": "Action to perform: 'create', 'get', 'list', 'update', 'stop'."
            },
            "task_id": {
                "type": "STRING",
                "description": "Optional: ID of the task to update, get, or stop."
            },
            "task_details": {
                "type": "STRING",
                "description": "Optional: Description or payload for creating/updating tasks."
            }
        },
        "required": ["action"]
    }
}

spawn_subagent = {
    "name": "spawn_subagent",
    "description": "Spins up a parallel sub-agent to handle a specific lane of work.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "objective": {
                "type": "STRING",
                "description": "Detailed instructions on what the sub-agent needs to accomplish."
            },
            "working_directory": {
                "type": "STRING",
                "description": "The directory the sub-agent should operate within."
            }
        },
        "required": ["objective"]
    }
}

scratchpad_edit = {
    "name": "scratchpad_edit",
    "description": "Writes down plans, todos, or notes to an internal memory notebook.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "content": {
                "type": "STRING",
                "description": "The notes or plans to save."
            }
        },
        "required": ["content"]
    }
}

# Combine all tools into a single list to pass to the Gemini SDK
AGENT_TOOLS = [
    read_file,
    write_file,
    edit_file,
    list_directory,
    grep_search,
    web_search,
    web_fetch,
    tool_search,
    bash_execute,
    lsp_query,
    task_registry,
    spawn_subagent,
    scratchpad_edit
]

# Example Usage:
# import google.generativeai as genai
# model = genai.GenerativeModel(model_name='gemini-1.5-pro', tools=AGENT_TOOLS)

import argparse
import json
import os
import glob
import re
try:
    from googlesearch import search
except ImportError:
    print(json.dumps({"error": "googlesearch library not found. Please install it using 'pip install googlesearch-python'"}))
    exit()
try:
    import requests
except ImportError:
    print(json.dumps({"error": "requests library not found. Please install it using 'pip install requests'"}))
    exit()

def do_read_file(args):
    try:
        with open(args.file_path, 'r') as f:
            content = f.read()
        print(json.dumps({"content": content}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_write_file(args):
    try:
        with open(args.file_path, 'w') as f:
            f.write(args.content)
        print(json.dumps({"success": True}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_edit_file(args):
    try:
        with open(args.file_path, 'r') as f:
            content = f.read()
        new_content = content.replace(args.search_string, args.replace_string)
        with open(args.file_path, 'w') as f:
            f.write(new_content)
        print(json.dumps({"success": True}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_list_directory(args):
    try:
        if args.pattern:
            files = glob.glob(os.path.join(args.directory_path, args.pattern), recursive=True)
        else:
            files = os.listdir(args.directory_path)
        print(json.dumps({"files": files}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_grep_search(args):
    try:
        results = []
        for dirpath, _, filenames in os.walk(args.directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r') as f:
                        for line_num, line in enumerate(f, 1):
                            if re.search(args.regex_pattern, line):
                                results.append({"file_path": file_path, "line_number": line_num, "line": line.strip()})
                except Exception:
                    # Ignore files that can't be opened
                    pass
        print(json.dumps({"results": results}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_web_search(args):
    try:
        print(f"Searching for: {args.query}")
        results = [r for r in search(args.query, num_results=args.num_results or 10)]
        print(f"Found {len(results)} results.")
        print(json.dumps({"results": results}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_web_fetch(args):
    try:
        response = requests.get(args.url)
        print(json.dumps({"content": response.text}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_tool_search(args):
    try:
        tools_list = [tool['name'] for tool in AGENT_TOOLS]
        print(json.dumps({"tools": tools_list}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_bash_execute(args):
    import subprocess
    try:
        if args.background:
            process = subprocess.Popen(args.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(json.dumps({"success": True, "pid": process.pid, "message": "Started in background"}))
        else:
            result = subprocess.run(args.command, shell=True, capture_output=True, text=True)
            print(json.dumps({
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_lsp_query(args):
    print(json.dumps({"error": "LSP query is not yet fully implemented. Requires language server integration."}))

def do_task_registry(args):
    try:
        registry_path = os.path.join(os.path.dirname(__file__), 'task_registry.json')
        
        # Load existing
        if os.path.exists(registry_path):
            with open(registry_path, 'r') as f:
                tasks = json.load(f)
        else:
            tasks = {}
            
        if args.action == 'create':
            import uuid
            task_id = str(uuid.uuid4())
            tasks[task_id] = {"details": args.task_details, "status": "pending"}
            with open(registry_path, 'w') as f:
                json.dump(tasks, f, indent=2)
            print(json.dumps({"success": True, "task_id": task_id}))
            
        elif args.action == 'list':
            print(json.dumps({"tasks": tasks}))
            
        elif args.action == 'get':
            if args.task_id and args.task_id in tasks:
                print(json.dumps({"task": tasks[args.task_id]}))
            else:
                print(json.dumps({"error": "Task not found"}))
                
        elif args.action == 'update':
            if args.task_id and args.task_id in tasks:
                if args.task_details:
                    tasks[args.task_id]["details"] = args.task_details
                with open(registry_path, 'w') as f:
                    json.dump(tasks, f, indent=2)
                print(json.dumps({"success": True}))
            else:
                print(json.dumps({"error": "Task not found"}))
                
        elif args.action == 'stop':
            if args.task_id and args.task_id in tasks:
                tasks[args.task_id]["status"] = "stopped"
                with open(registry_path, 'w') as f:
                    json.dump(tasks, f, indent=2)
                print(json.dumps({"success": True}))
            else:
                print(json.dumps({"error": "Task not found"}))
        else:
            print(json.dumps({"error": "Invalid action"}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

def do_spawn_subagent(args):
    print(json.dumps({"error": "Spawn subagent is not yet fully implemented. Requires orchestration framework."}))

def do_scratchpad_edit(args):
    try:
        scratchpad_path = os.path.join(os.path.dirname(__file__), 'scratchpad.md')
        mode = 'a' if os.path.exists(scratchpad_path) else 'w'
        with open(scratchpad_path, mode) as f:
            f.write(args.content + "\n")
        print(json.dumps({"success": True, "message": f"Appended to {scratchpad_path}"}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Gemini-based coding agent.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # read_file
    read_file_parser = subparsers.add_parser("read_file")
    read_file_parser.add_argument("--file_path", required=True)
    read_file_parser.set_defaults(func=do_read_file)

    # write_file
    write_file_parser = subparsers.add_parser("write_file")
    write_file_parser.add_argument("--file_path", required=True)
    write_file_parser.add_argument("--content", required=True)
    write_file_parser.set_defaults(func=do_write_file)

    # edit_file
    edit_file_parser = subparsers.add_parser("edit_file")
    edit_file_parser.add_argument("--file_path", required=True)
    edit_file_parser.add_argument("--search_string", required=True)
    edit_file_parser.add_argument("--replace_string", required=True)
    edit_file_parser.set_defaults(func=do_edit_file)

    # list_directory
    list_directory_parser = subparsers.add_parser("list_directory")
    list_directory_parser.add_argument("--directory_path", required=True)
    list_directory_parser.add_argument("--pattern")
    list_directory_parser.set_defaults(func=do_list_directory)

    # grep_search
    grep_search_parser = subparsers.add_parser("grep_search")
    grep_search_parser.add_argument("--regex_pattern", required=True)
    grep_search_parser.add_argument("--directory_path", required=True)
    grep_search_parser.set_defaults(func=do_grep_search)

    # web_search
    web_search_parser = subparsers.add_parser("web_search")
    web_search_parser.add_argument("--query", required=True)
    web_search_parser.add_argument("--num_results", type=int)
    web_search_parser.set_defaults(func=do_web_search)

    # web_fetch
    web_fetch_parser = subparsers.add_parser("web_fetch")
    web_fetch_parser.add_argument("--url", required=True)
    web_fetch_parser.set_defaults(func=do_web_fetch)

    # tool_search
    tool_search_parser = subparsers.add_parser("tool_search")
    tool_search_parser.set_defaults(func=do_tool_search)

    # bash_execute
    bash_execute_parser = subparsers.add_parser("bash_execute")
    bash_execute_parser.add_argument("--command", required=True)
    bash_execute_parser.add_argument("--background", action="store_true")
    bash_execute_parser.set_defaults(func=do_bash_execute)

    # lsp_query
    lsp_query_parser = subparsers.add_parser("lsp_query")
    lsp_query_parser.add_argument("--query_type", required=True)
    lsp_query_parser.add_argument("--file_path", required=True)
    lsp_query_parser.add_argument("--line_number", type=int)
    lsp_query_parser.set_defaults(func=do_lsp_query)

    # task_registry
    task_registry_parser = subparsers.add_parser("task_registry")
    task_registry_parser.add_argument("--action", required=True)
    task_registry_parser.add_argument("--task_id")
    task_registry_parser.add_argument("--task_details")
    task_registry_parser.set_defaults(func=do_task_registry)

    # spawn_subagent
    spawn_subagent_parser = subparsers.add_parser("spawn_subagent")
    spawn_subagent_parser.add_argument("--objective", required=True)
    spawn_subagent_parser.add_argument("--working_directory")
    spawn_subagent_parser.set_defaults(func=do_spawn_subagent)

    # scratchpad_edit
    scratchpad_edit_parser = subparsers.add_parser("scratchpad_edit")
    scratchpad_edit_parser.add_argument("--content", required=True)
    scratchpad_edit_parser.set_defaults(func=do_scratchpad_edit)

    args = parser.parse_args()
    args.func(args)
