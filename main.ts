// Entry for make.fun bounty "Sum up 24 November's world news in one image"
// (news-image-20261124). The image beside this file, entry.png, is the entry:
// a one-page broadsheet summing up the world news of Tuesday 24 November 2026.
// It was drawn by build_image.py (also in this repo) from that day's reporting.
//
// The program copies entry.png to the output directory, byte for byte, so the
// two grading runs produce identical bytes. No network, no randomness.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

copyFileSync(
  new URL("./entry.png", import.meta.url),
  join(process.env.MAKEFUN_OUTPUT_DIR ?? "/output", "entry.png"),
);
