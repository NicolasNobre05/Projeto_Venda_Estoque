Criação do usuário e do banco de dados

CMD:

mysql -u root -p

CREATE USER 'UserProjetosVendas'@'%' IDENTIFIED BY 'ProjetosVendas';

CREATE DATABASE projetosvendasestoque;

GRANT ALL PRIVILEGES ON `projetosvendasestoque`.* TO 'UserProjetosVendas'@'%';
GRANT PROCESS ON *.* TO 'UserProjetosVendas'@'%';
FLUSH PRIVILEGES;


mysql -u UserProjetosVendas -p

USE projetosvendasestoque;

