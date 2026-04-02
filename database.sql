DROP TABLE IF EXISTS financements CASCADE;
DROP TABLE IF EXISTS type_financement CASCADE;
DROP TABLE IF EXISTS credit_bancaire CASCADE;
DROP TABLE IF EXISTS type_credit_bancaire CASCADE;
DROP TABLE IF EXISTS soutien_public CASCADE;
DROP TABLE IF EXISTS type_soutien_public CASCADE;
DROP TABLE IF EXISTS assurances_agricoles CASCADE;
DROP TABLE IF EXISTS type_assurance_agricole CASCADE;
DROP TABLE IF EXISTS recensements CASCADE;

CREATE TABLE IF NOT EXISTS recensements(
 id SERIAL PRIMARY KEY,
 nom_exploitant VARCHAR(100),
 prenom VARCHAR(100),
 wilaya VARCHAR(100),
 commune VARCHAR(100)
);

INSERT INTO recensements (nom_exploitant, prenom, wilaya, commune) VALUES
('بن علي','أحمد','تيارت','تيارت'),
('زروقي','فاطمة','الجزائر','الجزائر الوسطى');

SELECT * FROM recensements;

CREATE TABLE type_financement(
 id SERIAL PRIMARY KEY,
 nom_fr VARCHAR(150),
 nom_ar VARCHAR(150)
);

INSERT INTO type_financement (nom_fr, nom_ar) VALUES
('Ressources propres','موارد ذاتية'),
('Crédit bancaire','قرض بنكي'),
('Soutien public','دعم عمومي'),
('Emprunt à un tiers','قرض من الغير');

SELECT * FROM type_financement;

CREATE TABLE financements(
 recensement_id INT,
 type_financement_id INT,
 PRIMARY KEY(recensement_id,type_financement_id),
 FOREIGN KEY(recensement_id) REFERENCES recensements(id),
 FOREIGN KEY(type_financement_id) REFERENCES type_financement(id)
);

INSERT INTO financements VALUES
(1,1),
(1,2);

SELECT * FROM financements;

CREATE TABLE type_credit_bancaire(
 id SERIAL PRIMARY KEY,
 nom_fr VARCHAR(150),
 nom_ar VARCHAR(150)
);

INSERT INTO type_credit_bancaire (nom_fr, nom_ar) VALUES
('Ettahadi','الاتحادي'),
('Classique','كلاسيكي'),
('Leasing','إيجار تمويلي'),
('Rfig','رفيق');

SELECT * FROM type_credit_bancaire;

CREATE TABLE credit_bancaire(
 recensement_id INT,
 type_credit_id INT,
 PRIMARY KEY(recensement_id,type_credit_id),
 FOREIGN KEY(recensement_id) REFERENCES recensements(id),
 FOREIGN KEY(type_credit_id) REFERENCES type_credit_bancaire(id)
);

INSERT INTO credit_bancaire VALUES
(1,1),
(1,4);

SELECT * FROM credit_bancaire;

CREATE TABLE type_soutien_public(
 id SERIAL PRIMARY KEY,
 nom_fr VARCHAR(150),
 nom_ar VARCHAR(150)
);

INSERT INTO type_soutien_public (nom_fr, nom_ar) VALUES
('Financier','مالي'),
('Matériel','عتاد'),
('Cultures','محاصيل');

SELECT * FROM type_soutien_public;

CREATE TABLE soutien_public(
 recensement_id INT,
 type_soutien_id INT,
 PRIMARY KEY(recensement_id,type_soutien_id),
 FOREIGN KEY(recensement_id) REFERENCES recensements(id),
 FOREIGN KEY(type_soutien_id) REFERENCES type_soutien_public(id)
);

INSERT INTO soutien_public VALUES
(1,1),
(1,2);

SELECT * FROM soutien_public;

CREATE TABLE type_assurance_agricole(
 id SERIAL PRIMARY KEY,
 nom_fr VARCHAR(150),
 nom_ar VARCHAR(150)
);

INSERT INTO type_assurance_agricole (nom_fr, nom_ar) VALUES
('Terre','الأرض'),
('Personnel','العمال'),
('Cultures','المحاصيل'),
('Bâtiments','المباني'),
('Matériels','العتاد'),
('Cheptel','المواشي');

SELECT * FROM type_assurance_agricole;

CREATE TABLE assurances_agricoles(
 recensement_id INT,
 type_assurance_id INT,
 PRIMARY KEY(recensement_id,type_assurance_id),
 FOREIGN KEY(recensement_id) REFERENCES recensements(id),
 FOREIGN KEY(type_assurance_id) REFERENCES type_assurance_agricole(id)
);

INSERT INTO assurances_agricoles VALUES
(1,3),
(1,6);

SELECT * FROM assurances_agricoles;


SELECT
r.nom_exploitant,
r.prenom,
tf.nom_fr AS financement,
tc.nom_fr AS credit_bancaire,
ts.nom_fr AS soutien_public,
ta.nom_fr AS assurance_agricole

FROM recensements r

LEFT JOIN financements f
ON r.id = f.recensement_id
LEFT JOIN type_financement tf
ON tf.id = f.type_financement_id

LEFT JOIN credit_bancaire cb
ON r.id = cb.recensement_id
LEFT JOIN type_credit_bancaire tc
ON tc.id = cb.type_credit_id

LEFT JOIN soutien_public sp
ON r.id = sp.recensement_id
LEFT JOIN type_soutien_public ts
ON ts.id = sp.type_soutien_id

LEFT JOIN assurances_agricoles aa
ON r.id = aa.recensement_id
LEFT JOIN type_assurance_agricole ta
ON ta.id = aa.type_assurance_id;
