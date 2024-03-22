-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 22-Mar-2024 às 01:50
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bd_navarro`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `bancos_consultas`
--

CREATE TABLE `bancos_consultas` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `data_publicacao` varchar(20) DEFAULT NULL,
  `lucro_liquido` varchar(20) DEFAULT NULL,
  `patrimonio_liquido` varchar(20) DEFAULT NULL,
  `ativo_total` varchar(20) DEFAULT NULL,
  `captacoes` varchar(20) DEFAULT NULL,
  `carteira_credito_classificada` varchar(20) DEFAULT NULL,
  `patrimonio_referencia_rwa` varchar(20) DEFAULT NULL,
  `numero_agencias` int(11) DEFAULT NULL,
  `numero_pontos_atendimento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `bancos_consultas`
--

INSERT INTO `bancos_consultas` (`id`, `nome`, `data_publicacao`, `lucro_liquido`, `patrimonio_liquido`, `ativo_total`, `captacoes`, `carteira_credito_classificada`, `patrimonio_referencia_rwa`, `numero_agencias`, `numero_pontos_atendimento`) VALUES
(1, 'c6', '06/2023', '-123,3 milhões', '3,3 bilhões', '55,7 bilhões', '41,5 bilhões', '37,7 bilhões', '3,6 bilhões', 6, 1),
(2, 'bradesco', '06/2023', '4,5 bilhões', '160,4 bilhões', '1,6 trilhão', '1,2 trilhão', '627,1 bilhões', '148,6 bilhões', 3, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `bancos_consultas`
--
ALTER TABLE `bancos_consultas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nome` (`nome`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `bancos_consultas`
--
ALTER TABLE `bancos_consultas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
