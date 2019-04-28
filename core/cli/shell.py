#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from cmd import Cmd
from core.cli.commands import ShellCommands
from core.utils.helpers import get_modules

class Shell(ShellCommands, Cmd):
    namespace = ""
    module = ""
    modules = get_modules()
    intro = "Welcome to the grapheneX interactive shell. Type \"help\" or \"?\" to list commands."

    @property
    def prompt(self):
        prompt_str = ""
        if self.namespace:
            prompt_str = prompt_str + ":" + self.namespace
        if self.module:
            prompt_str = prompt_str + ":" + self.module
        return f"[gX{prompt_str}]> "