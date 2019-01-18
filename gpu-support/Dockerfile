FROM tensorflow/tensorflow:latest-gpu-py3

ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"

COPY . /home/foo/namefriend-camo
WORKDIR /home/foo/namefriend-camo
CMD ["/bin/bash"]

RUN \
  adduser foo --home /home/foo --shell /bin/bash --disabled-password --gecos "" &&\
  touch /home/foo/.sudo_as_admin_successful &&\
  chown -R foo:foo /home/foo &&\
  usermod -a -G sudo foo &&\
  apt-get update &&\
  apt-get install -y sudo git-core python3-pip &&\
  echo '%sudo ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/nopass

USER foo

RUN \
  pip3 install --user pipenv &&\
  echo '\nexport PATH="/home/foo/.local/bin:$PATH"\nexport LC_ALL=C.UTF-8\nexport LANG=C.UTF-8\n' >> /home/foo/.bashrc &&\
  /home/foo/.local/bin/pipenv install
