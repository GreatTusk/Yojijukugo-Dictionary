/* User creation
CREATE USER dictionary IDENTIFIED BY "Contrasena.123"
DEFAULT TABLESPACE DATA
TEMPORARY TABLESPACE temp
QUOTA UNLIMITED ON DATA;
GRANT RESOURCE TO dictionary;
GRANT CREATE SESSION TO dictionary;
*/
GRANT CREATE VIEW TO dictionary;

/*Table creation*/
DROP TABLE yojijukugo CASCADE CONSTRAINTS;
DROP TABLE language CASCADE CONSTRAINTS;
DROP TABLE definition CASCADE CONSTRAINTS;
DROP TABLE sentence_sample CASCADE CONSTRAINTS;
DROP TABLE reading CASCADE CONSTRAINTS;

DROP SEQUENCE seq_yojijukugo;
DROP SEQUENCE seq_lan;

CREATE SEQUENCE seq_yojijukugo;
CREATE SEQUENCE seq_lan;


CREATE TABLE yojijukugo (
    id NUMBER (4) NOT NULL,
    word VARCHAR(12) NOT NULL,
    CONSTRAINT pk_yojijukugo PRIMARY KEY (id),
    CONSTRAINT uk_word UNIQUE (word)
);

CREATE TABLE reading (
     id NUMBER(4)  GENERATED ALWAYS AS IDENTITY NOT NULL,
     id_yojijukugo NUMBER(4) NOT NULL,
     reading VARCHAR(100) NOT NULL,
     CONSTRAINT fk_red_yoj FOREIGN KEY (id_yojijukugo) REFERENCES yojijukugo(id),
     CONSTRAINT pk_reading PRIMARY KEY (id, id_yojijukugo)
);

CREATE TABLE language (
    id NUMBER (3) NOT NULL,
    language VARCHAR(20) NOT NULL,
    CONSTRAINT pk_language PRIMARY KEY (id)
);

CREATE TABLE definition (
    id NUMBER(6) GENERATED ALWAYS AS IDENTITY,
    id_language NUMBER(3) NOT NULL,
    id_yojijukugo NUMBER(4) NOT NULL,
    definition VARCHAR(255) NOT NULL,
    CONSTRAINT pk_definition PRIMARY KEY (id),
    CONSTRAINT fk_def_lan FOREIGN KEY (id_language) REFERENCES language(id),
    CONSTRAINT fk_def_yoj FOREIGN KEY (id_yojijukugo) REFERENCES yojijukugo(id)
);


CREATE TABLE sentence_sample(
    id_language NUMBER(3) NOT NULL,
    id_yojijukugo NUMBER(4) NOT NULL,
    sentence VARCHAR(255) NOT NULL,
    CONSTRAINT pk_sen PRIMARY KEY (id_language, id_yojijukugo, sentence),
    CONSTRAINT fk_sen_lan FOREIGN KEY (id_language) REFERENCES language(id),
    CONSTRAINT fk_sen_yoj FOREIGN KEY (id_yojijukugo) REFERENCES yojijukugo(id)
);

/*language*/

INSERT INTO language (id, language) VALUES (seq_lan.NEXTVAL, 'Japanese');
INSERT INTO language (id, language) VALUES (seq_lan.NEXTVAL, 'Spanish');
INSERT INTO language (id, language) VALUES (seq_lan.NEXTVAL, 'English');
/*definition*/

--separate file

/*data insertion for yojijukugo*/

--yojijukugo.sql

--SELECT * FROM NLS_DATABASE_PARAMETERS WHERE PARAMETER = 'NLS_CHARACTERSET';

