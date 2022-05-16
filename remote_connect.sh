#!/bin/bash
HOST=""
USER=""
LOCAL_HOST=localhost
LOCAL_ANNOTATOR_PORT=8003
IMAGE_PORT=6008
REMOTE_ANNOTATOR_PORT=8003

print_modes() {
	echo "-----MENU-----"
	echo "1: connect to remote annotator"
	echo "2: disconnect from remote annotator"
	echo "0: quit"
	echo
	echo -n "type mode and presss [enter]: "
}

print_modes

while true; do
	read MODE

	if [ "$MODE" == "1" ];
	then
		echo "----------"
		echo "Enter the GPU server user name: "  
		read USER  
		echo "The Current User Name is $USER"
		echo  
		echo "Enter GPU server IP: "  
		read HOST
		echo "GPU server access on $USER:$HOST"
		echo 
		echo "establishing connection to annotator..."
		echo "password: "
		ssh -N -f -L $LOCAL_HOST:$LOCAL_ANNOTATOR_PORT:$LOCAL_HOST:$REMOTE_ANNOTATOR_PORT $USER@$HOST
		echo "----------"
		echo "establishing connection to image server..."
		echo "password: "
		ssh -N -f -L $LOCAL_HOST:$IMAGE_PORT:$LOCAL_HOST:$IMAGE_PORT $USER@$HOST
		echo "Running annotator on $LOCAL_HOST:$LOCAL_ANNOTATOR_PORT"
		break

	elif [ "$MODE" == "2" ];
	then
		echo "disconnecting from remote annotator..."
		lsof -ti:$LOCAL_ANNOTATOR_PORT | xargs kill -9
		echo "disconnecting from image server..."
		lsof -ti:$IMAGE_PORT | xargs kill -9
		break

	elif [ "$MODE" == "0" ];
	then
		break

	else
		echo 
		echo "ERROR: wrong input no input: " $MODE
		print_modes
	fi
done