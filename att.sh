#!/bin/bash

alias quit=exit

STATE=0

function block() {
	python3 att.py $1
	echo
	if [ "$2" ]; then
		sleep $2
	fi
}

function prompt() {
	echo -n "> "
	read response
	eval $response
}

function look() {
	if [ "$1" == "picture" ]; then
		echo "You look at the PICTURE OF THE MOON. It is a picture of the moon."
	fi
}

function start() {
	if [ "$1" == "conveyor" ]; then
		if [ $STATE == 0 ]; then
			block conveyor1 1
			block conveyor2 1
			block conveyor3 1
			STATE=1
			
			block conveyor_start
		else
			block conveyor_running
		fi
	fi
}

clear
block intro 3
clear
block g1 3
block g2 3
block g3 3
block g4
while true; do prompt; done

