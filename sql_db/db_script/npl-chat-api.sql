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
  `user_name` BLOB(256) NOT NULL,
  `un_salt` BINARY(64) NOT NULL,
  `user_lastname` BLOB(256) NOT NULL,
  `uln_salt` BINARY(64) NOT NULL,
  `user_mail` BLOB(256) NOT NULL,
  `um_salt` BINARY(64) NOT NULL,
  `user_nick` VARCHAR(45) NOT NULL,
  `user_pass` BLOB(256) NOT NULL,
  `up_salt` BINARY(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_nick_UNIQUE` (`user_nick` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nlp_chat_api`.`users_has_chats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`users_has_chats` (
  `chat_id` INT NOT NULL AUTO_INCREMENT,
  `chat_name` VARCHAR(45) NOT NULL,
  `user_1_id` INT NOT NULL,
  `user_2_id` INT NOT NULL,
  PRIMARY KEY (`chat_id`),
  INDEX `fk_users_has_chats_users1_idx` (`user_1_id` ASC) VISIBLE,
  INDEX `fk_users_has_chats_users2_idx` (`user_2_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_chats_users1`
    FOREIGN KEY (`user_1_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_chats_users2`
    FOREIGN KEY (`user_2_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nlp_chat_api`.`chat_messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`chat_messages` (
  `chat_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `message` VARCHAR(45) NOT NULL,
  `message_date` DATETIME NOT NULL,
  INDEX `fk_chat_messages_users_has_chats1_idx` (`chat_id` ASC) VISIBLE,
  INDEX `fk_chat_messages_users_has_chats2_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_chat_messages_users_has_chats1`
    FOREIGN KEY (`chat_id`)
    REFERENCES `nlp_chat_api`.`users_has_chats` (`chat_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_chat_messages_users_has_chats2`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_chats` (`user_1_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_chat_messages_users_has_chats3`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_chats` (`user_2_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nlp_chat_api`.`users_has_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`users_has_groups` (
  `group_id` INT NOT NULL AUTO_INCREMENT,
  `group_name` VARCHAR(45) NOT NULL,
  `user_id_admin` INT NOT NULL,
  `user_1_id` INT NULL,
  `user_2_id` INT NULL,
  `user_3_id` INT NULL,
  `user_4_id` INT NULL,
  `user_5_id` INT NULL,
  `user_6_id` INT NULL,
  `user_7_id` INT NULL,
  `user_8_id` INT NULL,
  `user_9_id` INT NULL,
  PRIMARY KEY (`group_id`),
  INDEX `fk_users_has_groups_users1_idx` (`user_id_admin` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users2_idx` (`user_1_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users3_idx` (`user_2_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users4_idx` (`user_3_id` ASC) VISIBLE,
  UNIQUE INDEX `group_id_UNIQUE` (`group_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users5_idx` (`user_4_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users6_idx` (`user_5_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users7_idx` (`user_6_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users8_idx` (`user_7_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users9_idx` (`user_8_id` ASC) VISIBLE,
  INDEX `fk_users_has_groups_users10_idx` (`user_9_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_groups_users1`
    FOREIGN KEY (`user_id_admin`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users2`
    FOREIGN KEY (`user_1_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users3`
    FOREIGN KEY (`user_2_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users4`
    FOREIGN KEY (`user_3_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users5`
    FOREIGN KEY (`user_4_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users6`
    FOREIGN KEY (`user_5_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users7`
    FOREIGN KEY (`user_6_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users8`
    FOREIGN KEY (`user_7_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users9`
    FOREIGN KEY (`user_8_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_groups_users10`
    FOREIGN KEY (`user_9_id`)
    REFERENCES `nlp_chat_api`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nlp_chat_api`.`group_messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nlp_chat_api`.`group_messages` (
  `group_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `group_name` VARCHAR(45) NOT NULL,
  `message` VARCHAR(45) NOT NULL,
  `message_date` DATETIME NOT NULL,
  INDEX `fk_group_messages_users_has_groups2_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_group_messages_users_has_groups1_idx` (`group_id` ASC) VISIBLE,
  CONSTRAINT `fk_group_messages_users_has_groups2`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_id_admin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups3`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_1_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups4`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_2_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups5`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_3_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups1`
    FOREIGN KEY (`group_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`group_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups6`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_4_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups7`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_5_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups8`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_6_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups9`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_7_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups10`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_7_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups11`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_8_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_messages_users_has_groups12`
    FOREIGN KEY (`user_id`)
    REFERENCES `nlp_chat_api`.`users_has_groups` (`user_9_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
