# 新的VPS centos 7,需要安装的一些软件,方法记录
## install epel
* yum install epel-release
## install R
* sudo yum install R
* sudo su - -c "R -e \"install.packages('shiny', repos='https://cran.rstudio.com/')\""
## install shiny-server
* wget https://download3.rstudio.org/centos5.9/x86_64/shiny-server-1.5.1.834-rh5-x86_64.rpm
* sudo yum install --nogpgcheck shiny-server-1.5.1.834-rh5-x86_64.rpm
## install Rstudio
* wget https://download2.rstudio.org/rstudio-server-rhel-1.0.136-x86_64.rpm
* sudo yum install --nogpgcheck rstudio-server-rhel-1.0.136-x86_64.rpm
  * note : 不支持root用户
## install sbt
* wget http://dl.bintray.com/sbt/rpm/sbt-0.13.5.rpm
* sudo yum localinstall sbt-0.13.5.rpm
  * 版本检测 sbt sbt-version


