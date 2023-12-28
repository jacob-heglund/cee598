
# start interactive docker container for running code
docker_int:
	docker run -it --rm \
		--user root \
		--gpus all \
		-v `pwd`:/cee598 \
		-t cee598:1.0 \
		bash

# start jupyter notebook (using jupyter lab) in docker container
docker_jup:
	docker run -it --rm \
		--user root \
		--gpus all \
		-p 8889:8889 \
		-v `pwd`:/cee598 \
		-t cee598:1.0 \
		jupyter lab --ip 0.0.0.0 --allow-root --port=8889

#TODO need to forward the port outside of the docker container

####################
# docker stuff
####################
containers:
	docker ps -a

images:
	docker image ls

nvidia:
	watch nvidia-smi

# change permissions of any created files so they can be deleted, moved, etc. without any issues (ownership of files created in docker container)
chown:
	sudo chown -R `whoami` .

