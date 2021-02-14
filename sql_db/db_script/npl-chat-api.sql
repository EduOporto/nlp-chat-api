-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema nlp_chat_api
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema nlp_chat_api
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `nlp_chat_api` ;
USE `nlp_chat_api` ;

-- -----------------------------------------------------
-- Table `nlp_chat_api`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` BLOB(256) NOT NULL,
  `n_salt` BINARY(64) NOT NULL,
  `lastname` BLOB(256) NOT NULL,
  `ln_salt` BINARY(64) NOT NULL,
  `email` BLOB(256) NOT NULL,
  `em_salt` BINARY(64) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` BLOB(256) NOT NULL,
  `p_salt` BINARY(64) NOT NULL,
  `confirmed_at` DATETIME NOT NULL,
  `last_login_at` DATETIME NULL,
  `login_count` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_nick_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nlp_chat_api`.`users_has_chats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`users_has_chats` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_a_id` INT NOT NULL,
  `user_b_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_chats_users1_idx` (`user_a_id` ASC) VISIBLE,
  INDEX `fk_users_has_chats_users2_idx` (`user_b_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_chats_users1`
    FOREIGN KEY (`user_a_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_chats_users2`
    FOREIGN KEY (`user_b_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nlp_chat_api`.`chat_messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`chat_messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `chat_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `message` VARCHAR(45) NOT NULL,
  `message_date` DATETIME NOT NULL,
  INDEX `fk_chat_messages_users_has_chats1_idx` (`chat_id` ASC) VISIBLE,
  INDEX `fk_chat_messages_users_has_chats2_idx` (`user_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_chat_messages_users_has_chats1`
    FOREIGN KEY (`chat_id`)
    REFERENCES `nlp_chat_api`.`users_has_chats` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_chat_messages_users_has_chats2`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_chats` (`user_a_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_chat_messages_users_has_chats3`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_chats` (`user_b_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nlp_chat_api`.`users_has_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`users_has_groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_name` VARCHAR(45) NOT NULL,
  `group_admin_id` INT NOT NULL,
  `user_b_id` INT NULL,
  `user_c_id` INT NULL,
  `user_d_id` INT NULL,
  `user_e_id` INT NULL,
  `user_f_id` INT NULL,
  `user_g_id` INT NULL,
  `user_h_id` INT NULL,
  `user_i_id` INT NULL,
  `user_j_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_groups_users1_idx` (`group_admin_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users2_idx` (`user_b_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users3_idx` (`user_c_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users4_idx` (`user_d_id` ASC) VISIBLE,
  UNIQUE INDEX `group_id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users5_idx` (`user_e_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users6_idx` (`user_f_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users7_idx` (`user_g_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users8_idx` (`user_h_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users9_idx` (`user_i_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users10_idx` (`user_j_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_groups_users1`
    FOREIGN KEY (`group_admin_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users2`
    FOREIGN KEY (`user_b_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users3`
    FOREIGN KEY (`user_c_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users4`
    FOREIGN KEY (`user_d_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users5`
    FOREIGN KEY (`user_e_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users6`
    FOREIGN KEY (`user_f_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users7`
    FOREIGN KEY (`user_g_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users8`
    FOREIGN KEY (`user_h_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users9`
    FOREIGN KEY (`user_i_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users10`
    FOREIGN KEY (`user_j_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nlp_chat_api`.`group_messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`group_messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `message` VARCHAR(45) NOT NULL,
  `message_date` DATETIME NOT NULL,
  INDEX `fk_group_messages_users_has_groups2_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_group_messages_users_has_groups1_idx` (`group_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_group_messages_users_has_groups2`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`group_admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups3`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_b_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups4`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_c_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups5`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_d_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups1`
    FOREIGN KEY (`group_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups6`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_e_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups7`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_f_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups8`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_g_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups9`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_h_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups10`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_h_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups11`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_i_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups12`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_j_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
