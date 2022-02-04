FROM jupyterhub/jupyterhub:2.1.1
RUN pip install --no-cache --upgrade jupyter
RUN pip install --no-cache dockerspawner
