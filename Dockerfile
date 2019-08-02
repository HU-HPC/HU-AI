FROM rocker/binder:3.5.3
ENV ROOT=TRUE
# Copy your repository contents to the image
COPY . ${HOME}

## Run an install.R script, if it exists.
RUN if [ -f install.R ]; then R --quiet -f install.R; fi
RUN pip install jupyterlab
