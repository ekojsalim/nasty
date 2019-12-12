#
# Copyright 2019 Lukas Schmelzeisen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from argparse import ArgumentParser
from pathlib import Path
from typing import Sequence

from overrides import overrides

from ..request_executor import RequestExecutor
from ._command import _Command


class _ExecutorCommand(_Command):
    @classmethod
    @overrides
    def command(cls) -> str:
        return "executor"

    @classmethod
    @overrides
    def aliases(cls) -> Sequence[str]:
        return "e"

    @classmethod
    @overrides
    def description(cls) -> str:
        return "Execute previously submitted requests."

    @classmethod
    @overrides
    def config_argparser(cls, argparser: ArgumentParser) -> None:
        g = argparser.add_argument_group(
            "Executor Arguments",
            "Requests can be submitted to a jobs file by using the -e (--to-executor) "
            "options of the other nasty commands and then executed via this command. "
            "This allows to operate in batch mode, track progress, and rerun "
            "uncompleted/failed requests.",
        )
        g.add_argument(
            "-e",
            "--executor-file",
            metavar="<FILE>",
            type=Path,
            required=True,
            help="File to which requests have been submitted.",
        )
        g.add_argument(
            "-o",
            "--out-dir",
            metavar="<DIR>",
            type=Path,
            required=True,
            help="Directory to which results will be written.",
        )

    @overrides
    def run(self) -> None:
        request_executor = RequestExecutor()
        request_executor.load_requests(self._args.executor_file)
        request_executor.execute(self._args.out_dir)
