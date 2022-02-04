# Configuration file for Jupyter Hub

c = get_config()

# spawn with Docker
c.JupyterHub.spawner_class = 'docker'

# Spawn containers from this image
c.DockerSpawner.image = 'codercom/code-server'

# Have the Spawner override the Docker entrypoint
c.DockerSpawner.extra_create_kwargs.update({
  'entrypoint': '/usr/bin/entrypoint.sh --bind-addr 0.0.0.0:8888 --auth none'
})

# Overwrite cmd
c.DockerSpawner.cmd = ""


# Connect containers to this Docker network
network_name = 'jupyterhub_network'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }

notebook_dir = '/home/coder'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

c.DockerSpawner.remove = True
c.DockerSpawner.debug = True

# The Hub should listen on all interfaces,
# so user servers can connect
c.JupyterHub.hub_ip = '0.0.0.0'
# this is the name of the 'service' in docker-compose.yml
c.JupyterHub.hub_connect_ip = 'hub'

#timeouts
c.Spawner.http_timeout = 60
c.Spawner.start_timeout = 60
c.Spawner.spawn_timeout = 60


# increase launch timeout because initial image pulls can take a while
#c.DockerSpawner.spawn_timeout = 60

c.ConfigurableHTTPProxy.should_start = False
c.ConfigurableHTTPProxy.api_url = 'http://chp:8001'

# Dummy authentication
from jupyterhub.auth import DummyAuthenticator

c.JupyterHub.authenticator_class = DummyAuthenticator
