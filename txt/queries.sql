
select * from yojijukugo order by 2;
select * from DEFINITION WHERE definition like 'No definition found for%';
DROP INDEX idx_yokijukugo;
CREATE UNIQUE INDEX idx_yokijukugo ON yojijukugo(word);


select 
 y.ID,word, r.id, r.reading 
from yojijukugo  y
left JOIN
    reading r on y.id = r.id_yojijukugo
order by 2;

CREATE OR REPLACE VIEW V_GETREADINGS AS
SELECT y1.id, LISTAGG(r1.reading, ',') WITHIN GROUP (ORDER BY r1.reading) AS all_readings
FROM yojijukugo y1
INNER JOIN reading r1 ON y1.id = r1.id_yojijukugo
GROUP BY y1.id;

SELECT * FROM V_GETREADINGS;

CREATE OR REPLACE VIEW V_GETDEFINITIONS AS
SELECT y1.id,
       LISTAGG(d1.definition, '/') WITHIN GROUP (ORDER BY d1.id) AS all_definitions,
       d1.id_language
FROM yojijukugo y1
INNER JOIN definition d1 ON y1.id = d1.id_yojijukugo
GROUP BY y1.id, d1.id_language;

CREATE INDEX idx_definition_fk ON definition(id_yojijukugo);

CREATE VIEW V_GET_SAMPLE_SENTENCES AS
SELECT y.id,
       LISTAGG(s.sentence, '/') WITHIN GROUP (ORDER BY y.id) AS all_sentences,
       s.id_language
FROM yojijukugo y
INNER JOIN sentence_sample s ON y.id = s.id_yojijukugo
GROUP BY y.id, s.id_language;


SELECT y.ID, y.word, r.id, r.reading
FROM yojijukugo y
LEFT JOIN reading r ON y.id = r.id_yojijukugo
WHERE y.word = '悪逆無道'
ORDER BY y.word, r.reading;
