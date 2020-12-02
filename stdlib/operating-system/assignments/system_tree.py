#!/usr/bin/env python

import os
import argparse


class FileTreeMaker:

    def _recurse(self, parent_path, file_list, prefix, output_buf, level):
        if len(file_list) == 0 \
            or (self.max_level != -1 and self.max_level <= level):
            return
        else:
            file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
            for idx, sub_path in enumerate(file_list):
                if any(exclude_name in sub_path for exclude_name in self.exn):
                    continue

                full_path = os.path.join(parent_path, sub_path)
                idc = "┣━"
                if idx == len(file_list) - 1:
                    idc = "┗━"

                if os.path.isdir(full_path) and sub_path not in self.exf:
                    output_buf.append("%s%s[%s]" % (prefix, idc, sub_path))
                    if len(file_list) > 1 and idx != len(file_list) - 1:
                        tmp_prefix = prefix + "┃  "
                    else:
                        tmp_prefix = prefix + "    "
                    self._recurse(full_path, os.listdir(full_path), tmp_prefix, output_buf, level + 1)
                elif os.path.isfile(full_path):
                    output_buf.append("%s%s%s" % (prefix, idc, sub_path))

    def make(self, args):
        self.root = args.root
        self.exf = args.exclude_folder
        self.exn = args.exclude_name
        self.max_level = args.max_level

        print("root:%s" % self.root)

        buf = []
        path_parts = self.root.rsplit(os.path.sep, 1)
        buf.append("[%s]" % (path_parts[-1],))
        self._recurse(self.root, os.listdir(self.root), "", buf, 0)

        output_str = "\n".join(buf)

        if len(args.output) != 0:
            with open(args.output, 'w') as of:
                of.write(output_str)
        return output_str


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", help="root of file tree", default=".")
    parser.add_argument("-o", "--output", help="output file name", default="")
    parser.add_argument("-xf", "--exclude_folder", nargs='*', help="exclude folder", default=[])
    parser.add_argument("-xn", "--exclude_name", nargs='*', help="exclude name", default=[])
    parser.add_argument("-m", "--max_level", help="max level", type=int, default=-1)
    args = parser.parse_args()
    print(FileTreeMaker().make(args))
