SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema game_info
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `game_info` ;

-- -----------------------------------------------------
-- Schema game_info
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `game_info` DEFAULT CHARACTER SET utf8 ;
USE `game_info` ;

-- -----------------------------------------------------
-- Table `coords`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `coords` (
  `coords_id` INT NOT NULL AUTO_INCREMENT,
  `x` INT NULL,
  `y` INT NULL,
  `map` VARCHAR(45) NULL,
  PRIMARY KEY (`coords_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colr`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colr` (
  `colr_id` INT NOT NULL AUTO_INCREMENT,
  `colr` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`colr_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `player` (
  `idPlayer` INT NOT NULL AUTO_INCREMENT,
  `player_name` VARCHAR(45) NOT NULL,
  `player_password` VARCHAR(45) NOT NULL,
  `coords_coords_id` INT NULL,
  `colr_colr_id` INT NULL,
  PRIMARY KEY (`idPlayer`),
  CONSTRAINT `fk_player_coords1`
    FOREIGN KEY (`coords_coords_id`)
    REFERENCES `coords` (`coords_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_colr1`
    FOREIGN KEY (`colr_colr_id`)
    REFERENCES `colr` (`colr_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- CREATE INDEX `fk_player_coords1_idx` ON `player` (`coords_coords_id` ASC) VISIBLE;

-- CREATE INDEX `fk_player_colr1_idx` ON `player` (`colr_colr_id` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO colr (colr) VALUES ('red.png'), ('blue.png'), ('yellow.png'), ('green.png')

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'simenerkul';