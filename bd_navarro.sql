-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24-Mar-2024 às 17:58
-- Versão do servidor: 10.4.28-MariaDB
-- versão do PHP: 8.2.4

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `info_bancos`
--

CREATE TABLE `info_bancos` (
  `id` int(11) NOT NULL,
  `nome_banco` varchar(20) NOT NULL,
  `matriz` varchar(100) DEFAULT NULL,
  `site_oficial` varchar(50) DEFAULT NULL,
  `consolidacao` varchar(50) DEFAULT NULL,
  `nome_fantasia` varchar(50) DEFAULT NULL,
  `razao_social` varchar(50) DEFAULT NULL,
  `cnpj` char(14) DEFAULT NULL,
  `data_de_abertura` varchar(20) DEFAULT NULL,
  `controle_acionario` varchar(50) DEFAULT NULL,
  `tipo_da_instituicao` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lucro_liquido_bancos`
--

CREATE TABLE `lucro_liquido_bancos` (
  `id` int(11) NOT NULL,
  `nome_banco` varchar(50) DEFAULT NULL,
  `ano` varchar(20) DEFAULT NULL,
  `resultado` varchar(20) DEFAULT NULL,
  `valor_rs` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lucro_liquido_trimestral_bancos`
--

CREATE TABLE `lucro_liquido_trimestral_bancos` (
  `id` int(11) NOT NULL,
  `nome_banco` varchar(50) DEFAULT NULL,
  `trimestre` varchar(50) DEFAULT NULL,
  `2T2023` varchar(20) DEFAULT NULL,
  `1T2023` varchar(20) DEFAULT NULL,
  `4T2022` varchar(20) DEFAULT NULL,
  `3T2022` varchar(20) DEFAULT NULL,
  `2T2022` varchar(20) DEFAULT NULL,
  `1T2022` varchar(20) DEFAULT NULL,
  `4T2021` varchar(20) DEFAULT NULL,
  `3T2021` varchar(20) DEFAULT NULL,
  `2T2021` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `bancos_consultas`
--
ALTER TABLE `bancos_consultas`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `info_bancos`
--
ALTER TABLE `info_bancos`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `lucro_liquido_bancos`
--
ALTER TABLE `lucro_liquido_bancos`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `lucro_liquido_trimestral_bancos`
--
ALTER TABLE `lucro_liquido_trimestral_bancos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `bancos_consultas`
--
ALTER TABLE `bancos_consultas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `info_bancos`
--
ALTER TABLE `info_bancos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `lucro_liquido_bancos`
--
ALTER TABLE `lucro_liquido_bancos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `lucro_liquido_trimestral_bancos`
--
ALTER TABLE `lucro_liquido_trimestral_bancos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
