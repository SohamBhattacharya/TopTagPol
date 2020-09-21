#!/bin/bash


tar -czvf \
    topTagPol_summary.tar.gz \
    documentation/resources \
    documentation/topTagPol_summary \
    $(for f in $(grep "\.pdf" documentation/topTagPol_summary/topTagPol_summary.tex | grep plots | grep -v "%"); do \
        echo $f | awk -F[{},] '{print $2}';
    done)
