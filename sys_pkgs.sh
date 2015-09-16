
sudo apt-get update

sudo add-apt-repository -y ppa:webupd8team/sublime-text-3
sudo add-apt-repository -y ppa:webupd8team/sublime-text-3
sudo add-apt-repository -y ppa:chris-lea/node.js
sudo apt-add-repository -y ppa:ansible/ansible

sudo apt-get update



sudo apt-get -y install python-virtualenv
sudo apt-get -y install git
sudo apt-get -y install vsftpd
sudo apt-get -y install openssh-server 
sudo apt-get -y install python-yaml
sudo apt-get -y install libyaml-dev libpython2.7-dev
sudo apt-get -y install python-mysqldb
sudo apt-get -y install libmysqlclient-dev
sudo apt-get -y install sublime-text-installer
sudo apt-get -y install meld
sudo apt-get -y install graphviz libgraphviz-dev pkg-config
sudo apt-get -y install libpq-dev python-dev
sudo apt-get -y install python-software-properties
sudo apt-get -y install nodejs npm
sudo apt-get -y install nodejs
sudo apt-get -y install npm
sudo apt-get -y install postgresql postgresql-contrib
sudo apt-get -y install anisble
sudo apt-get -y install software-properties-common
sudo apt-get -y install ansible
sudo apt-get -y install fabric
sudo apt-get -y install nodejs


# to enable virtualenvwrapper in bash 
sudo pip install virtualenvwrapper

# http://stackoverflow.com/questions/12232421/virtualenvwrapper-commands-arent-working
# append the following lines to  .bashrc file



echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

#  reload your profile
source ~/.bashrc


mkvirtualwrapper env1

workon env1

pip install -r requirements.txt

