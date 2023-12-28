# CEE 598 - Physics-Informed Machine Learning

## Environment Setup

The only reason I'm using Docker is because some of these assignments use Pytorch and DeepXDE, which means installing CUDA. This is to keep this version of CUDA self-contained so it doesn't interact with my other projects.

Set up basic docker environment

```bash
cd docker
bash build.sh
```

Then in the base directory, you can easily start the docker container using make commands.