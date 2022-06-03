# Your Development
### Getting Started
In order to use YourDevelopment to manage your local environments you need to install `docker`. The installation process varies based on your os. If you're not familiar with docker you can use `docker desktop` to get started.

### Describing your projects
I've included an example file `projects.example.json` to show the available keys. 
You must either copy this or create a file called `projects.json`.
Then you can add in the details of your projects.

### Creating the docker-compose.yml
Once you've set up your `projects.json` you can then run `make setup` this will then run a python container to generate the `docker-compose.yml` file that you'll use to run your environment.

### Running your environment
Once the `docker-compose.yml` file is created, you can either use that file as normal if you're familiar with docker or
for ease you can run `make start` to run it. You can then run `make stop` to tear down the environment.




### FAQ

Q: What is the redis password?

A: `password`