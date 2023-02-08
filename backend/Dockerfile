FROM crowdbotics/cb-django:3.8-slim-buster AS build

# Copy dependency management files and install app packages to /.venv
# COPY ./Pipfile ./Pipfile.lock ./modules/django_articles/dist/django_articles-0.1.tar.gz /
COPY ./Pipfile ./Pipfile.lock /
COPY ./modules/django_articles/ /modules/django_articles/

# RUN PIPENV_VENV_IN_PROJECT=1 pip3 install modules/django_articles/
RUN pipenv install --deploy
# RUN PIPENV_VENV_IN_PROJECT=1 pipenv install django_articles-0.1.tar.gz
# RUN PIPENV_VENV_IN_PROJECT=1 pip install -r requirements.txt


FROM crowdbotics/cb-django:3.8-slim-buster AS release
ARG SECRET_KEY

# Set Working directory
WORKDIR /opt/webapp

# Add runtime user with respective access permissions
RUN groupadd -r django \
  && useradd -d /opt/webapp -r -g django django \
  && chown django:django -R /opt/webapp
USER django

# Copy virtual env from build stage
COPY --chown=django:django --from=build /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Copy app source
COPY --chown=django:django . .

# Collect static files and serve app
RUN python3 manage.py collectstatic --no-input
CMD waitress-serve --port=$PORT juan06022023_dev_61588.wsgi:application
