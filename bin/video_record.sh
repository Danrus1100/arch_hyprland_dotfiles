#!/bin/bash
wf-recorder -g "$(slurp)" --audio --file=$(date +"~/recordings/recordind_%d.%m.%Y_%I:%M:%S.mp4")
