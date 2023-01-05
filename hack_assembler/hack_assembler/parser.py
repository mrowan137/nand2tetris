"""
Module for processing input HACK assembly language file.
The module contains a class `Parser` that has capability to process input HACK
assembly line-by-line, and extract info needed more machine-code translation.
`Parser` class has the following methods:
* `__init__(self, hack_asm_file)`: does initial cleaning of input HACK assembly
  code and initializes state variables `curr_command_idx_` and `curr_command_`
  to default values.
* `HasMoreCommands(self)`: returns whether there are more commands to process.
* `Advance(self)`: iterates state to correspond to next HACK assembly command.
* `Reset(self)`: resets `curr_command_idx_` and `curr_command_` to their default
  values (they reference a command after calling `Advance` method).
* `CommandType(self)`: return the type of command (A-, C-, or L-).
* `Symbol(self)`: return the label name in a label `(aaa)` or `@aaa` command.
* `Dest(self)`: returns `dest` (destination) part of C-command.
* `Comp(self)`: returns `comp` (comparison) part of C-command.
* `Jump(self)`: returns `jump` (jump to address) part of a C-command.

Example usage:

```python
>>> parser = Parser(hack_asm_file)
>>> parser.Advance()
```

With this, parser would be on the first command in the input HACK assembly file.
Method `CommandType` could be used to check whether the current line corresponds
to A-, C-, or L- command. If it's an A-command, e.g., `Symbol` method can be
used to extract out the symbol name. If it's a C-command, `Dest`, `Comp`, or
`Jump` methods could be used to extract out the C-command fields.
"""


class Parser:
  """
  `Parser` is a tool for processing input HACK assembly language file.
  It provides simplifications to the original input file, storing these into a
  list which can be iterated. At each iteration, `Parser` contains state
  information about the current command, index of the current command, whether
  there are more commands to process, and the 'type' of the current command
  (A-, C-, or L-command). Additionally, `Parser` has capability to decompose
  C-commands into respective fields, which provides the necessary input for
  `Code` object to complete the translation from HACK assembly to machine code.
  """
  def __init__(self, hack_asm_file):
    """
    Initializes the `Parser` with input HACK assembly file `hack_asm_file` and
    filters out comments, whitespace, and newlines; the resulting list of
    commands is stored in member `commands_`. Index to the current command, and
    the current command itself are initialized to default values -1 and `None`
    respectively, meaning that the index `curr_command_idx_` does not point to
    a command, and `curr_command_` does not yet refer to a command (this is
    deferred to the `Advance` method, given there are commands to process).
    """
    self.hack_asm_file_ = hack_asm_file

    # parse the commands into list, ignore whiteline and comments
    self.commands_ = []
    with open(hack_asm_file, "r") as f:
      for line in f:
        if line: # ignore whitelines
          # ignore comment
          comment_start = line.find("//")
          if comment_start != -1:
            line = line[:comment_start]

          # ignore any whitespace
          while line.find(" ") != -1:
            line = line.replace(" ", "")

          # ignore any newline
          while line.find("\n") != -1:
            line = line.replace("\n", "")

          # add the line if there's anything left to add
          if line:
            self.commands_.append(line)

    # index for the current command
    self.curr_command_idx_ = -1
    self.curr_comand_ = None

  def HasMoreCommands(self):
    """
    Returns `true` if more commands to process, `false` otherwise.
    """
    return self.commands_ and (self.curr_command_idx_ < len(self.commands_) - 1)

  def Advance(self):
    """
    Read next command from input file, make it current command;
    Return `true` if advanced a line, return `false` otherwise.
    """
    if self.HasMoreCommands():
      self.curr_command_idx_ += 1
      self.curr_command_ = self.commands_[self.curr_command_idx_]
      return True
    else:
      return False

  def Reset(self):
    """
    Reinitializes the current command index, and current command.
    """
    self.curr_command_idx_ = -1
    self.curr_command_ = None

  def CommandType(self):
    """
    Returns the type of the current command:
      - "A_COMMAND": command has `@aaa` format
      - "C_COMMAND": command has `dest=comp;jump` format
      - "L_COMMAND": command has `(aaa)` format (aaa is a symbol)
    If no `curr_command_`, return `None`.
    """
    if not self.curr_command_:
      return None

    if self.curr_command_.find("@") != -1:
      return "A_COMMAND"
    elif (   self.curr_command_.find("=") != -1
          or self.curr_command_.find(";") != -1):
      # either '=' or ';' could be omitted in a C-command,
      # but there will be at least one
      return "C_COMMAND"
    else:
      # it is assumed the input commands are all accurate,
      # and there's only A-, C-, or L-command
      return "L_COMMAND"

  def Symbol(self):
    """
    Return the `aaa` part of a `@aaa` or `(aaa)` command.
    """
    res = None
    if self.CommandType() == "A_COMMAND":
      res = self.curr_command_.replace("@", "")
    elif self.CommandType() == "L_COMMAND":
      res = self.curr_command_.replace("(", "").replace(")", "")

    return res

  def Dest(self):
    """
    Returns the `dest` part of a C-command.
    """
    res = None
    if self.CommandType() == "C_COMMAND":
      if self.curr_command_.find("=") != -1:
        # command format: `dest=comp;jump` or `dest=comp`
        res = self.curr_command_.split("=")[0]
      else:
        # command format: `comp;jump`
        res = "null"

    return res

  def Comp(self):
    """
    Returns the `comp` part of a C-command.
    """
    res = None
    if self.CommandType() == "C_COMMAND":
      if self.curr_command_.find("=") != -1:
        # command format: `dest=comp;jump` or `dest=comp`
        res = self.curr_command_.split("=")[1].split(";")[0]
      else:
        # command format: `comp;jump`
        res = self.curr_command_.split(";")[0]

    return res

  def Jump(self):
    """
    Returns the `jump` part of a C-command.
    """
    res = None
    if self.CommandType() == "C_COMMAND":
      if self.curr_command_.find(";") != -1:
        # command format: `dest=comp;jump` or `comp;jump`
        res = self.curr_command_.split("=")[-1].split(";")[-1]
      else:
        # command format: `dest=comp`
        res = "null"

    return res
