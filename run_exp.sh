#!/bin/bash
for periodScalr in 2 5 10 20 50
do
    for taskLen in 100 1000 10000
        do
	    total_time=37687
	    series_len=$total_time*$periodScalr/$taskLen
	    series_len=$((${series_len//.*/+1}))
            echo '----------------------------'
            echo 'periodScalar:'$periodScalr
            echo 'taskLen:'$taskLen
	    echo 'series_len'$series_len
            #sed  -i '' '1s/.*$/Hi/g' ./config.tgffopt
            sed -i  "23s/.*$/series_len $series_len 3/g" ./config.tgffopt
            sed -i  "39s/.*$/type_attrib exec_time $taskLen 20/g" ./config.tgffopt
            ./tgff config
            ./python main.py
        done
done
