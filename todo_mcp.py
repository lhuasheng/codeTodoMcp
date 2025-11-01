
from fastmcp import FastMCP
# TODO: Add module-level docstring describing the purpose of this file
from typing import Annotated,NamedTuple
from todo_db import TodoDB
from dataclasses import dataclass


mcp = FastMCP(name="TodoServer")
todo_db = TodoDB()

# TODO: Add error handling for database operations

@mcp.tool(
        name="add_todo",
        description="Add a TODO to a file at a specific line number."
)
def add_todo(
        filename: Annotated[str, "Source file containing the #TODO"],
        text: Annotated[str, "Text of the TODO comment"],
        line_number: Annotated[int, "Line number of the TODO comment"]
) -> bool:
        """Add a TODO to a file at a specific line number."""
        # TODO: Validate input parameters (filename, text, line_number)
        return todo_db.add(filename, text, line_number)

@mcp.tool(
        name="get_todos_for_file",
        description="Get all TODO comments for a given source file. Returns empty array if none."
)
def get_todos_for_file(
        filename: Annotated[str, "Source file to get TODOs for"]
) -> list[str]:
        """Get all TODO comments for a given source file. Returns empty array if none."""
        todos = todo_db.get(filename)
        # TODO: Handle case when file does not exist in DB
        return [txt for txt in todos.values()]

@mcp.tool(
        name="delete_todos",
        description="Delete all TODOs for a file."
)
def delete_todos(
        filename: Annotated[str, "Source file to delete TODOs for"]
) -> None:
        """Delete all TODOs for a file."""
        # TODO: Confirm deletion with user before proceeding
        todo_db.delete_todos(filename)

@mcp.tool(
        name="count_todos",
        description="Count the number of TODOs in a file."
)
def count_todos(
        filename: Annotated[str, "Source file to count TODOs for"]
) -> int:
        """Count the number of TODOs in a file."""
        # TODO: Add logging for count operations
        return todo_db.count(filename)

@mcp.tool(
        name="get_todo_by_id",
        description="Get a TODO by its ID for a file."
)
def get_todo_by_id(
        filename: Annotated[str, "Source file"],
        id: Annotated[int, "TODO ID"]
) -> str:
        # TODO: Add input validation for TODO ID
        """Get a TODO by its ID for a file."""
        return todo_db.get_by_id(filename, id)

@mcp.tool(
        name="get_filenames",
        description="Get all filenames with TODOs."
)
def get_filenames() -> list[str]:
        """Get all filenames with TODOs."""
        return todo_db.get_filenames()

@mcp.tool(
        name="sample_data",
        description="Populate the database with sample data."
)
def sample_data() -> None:
        """Populate the database with sample data."""
        todo_db.sample_data()



@dataclass
class Todo:
    """
    Represent a TODO comment found in a source file.
    Attributes:
        filename (str): Path to the source file containing the #TODO.
        text (str): Text of the TODO comment.
        line_number (int): 1-based line number where the TODO comment appears.
    Methods:
        to_dict() -> dict:
            Return a dictionary with keys "filename", "text", and "line_number".
    Example:
        >>> todo = Todo()
        >>> todo.filename = "/path/to/file.py"
        >>> todo.text = "Refactor this function to improve performance"
        >>> todo.line_number = 42
        >>> todo.to_dict()
        {'filename': '/path/to/file.py', 'text': 'Refactor this function to improve performance', 'line_number': 42}
    """
    filename: Annotated[str, "Source file containing the #TODO"]
    text: Annotated[str, "Text of the TODO comment"]
    line_number: Annotated[int, "Line number of the TODO comment"]



    def to_dict(self) -> dict:
        return {
            "filename": self.filename,
            "text": self.text,
            "line_number": self.line_number,
        }


@mcp.tool(
    name="add_todos",
    description="Add multiple TODOs to their respective files."
)
def add_todos(todos: list[Todo]) -> list[bool]:
    for todo in todos:
        todo_db.add(todo.filename, todo.text, todo.line_number)
    return [True] * len(todos)

def main():
    mcp.run()

if __name__ == "__main__":
        main()