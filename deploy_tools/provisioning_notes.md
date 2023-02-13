Provisioning a New Site
=======================

## Required Packages

* nginx
* Python 3.10
* virtualenv + pip
* Git

eg, on Ubuntu:

# install dependencies
apt update
apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev liblzma-dev git

# download and compile openssl
curl -L https://www.openssl.org/source/openssl-1.1.1s.tar.gz | (cd /usr/src; tar xz)
cd /usr/src/openssl-1.1.1s && ./config --prefix=/usr/local && make -j4 && make install

# download and configure pyenv
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

echo >> ~/.bashrc # add new-line.
echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

# build python 3.9.16 with pyenv
CONFIGURE_OPTS="--with-openssl=/usr/local --with-openssl-rpath=auto" pyenv install 3.9.16

# build python 3.10.9 with pyenv
CONFIGURE_OPTS="--with-openssl=/usr/local --with-openssl-rpath=auto" pyenv install 3.10.9

## Nginx Virtual Host Config

* see nginx.template.conf
* Replace SITENAME with e.g. staging.domain.com

## Systemd Service

* see gunicorn-systemd.template.service
* replace SITENAME with e.g. staging.domain.com

## Folder Structure

Assume we have a user account at /home/username

/home/username
|---sites
    |---SITENAME
        |---database
        |---source
        |---static
        |---virtualenv
