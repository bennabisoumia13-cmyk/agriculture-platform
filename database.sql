--
-- PostgreSQL database dump
--

\restrict Hxn7gRDTneYAlLvnRjTVxJvm3T4a9lrqpo53WT3zXu7803ESCmG6xtqIYZsWl05

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

-- Started on 2026-04-02 23:40:31

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 232 (class 1259 OID 17848)
-- Name: assurances_agricoles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assurances_agricoles (
    recensement_id integer NOT NULL,
    type_assurance_id integer NOT NULL
);


ALTER TABLE public.assurances_agricoles OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 17798)
-- Name: credit_bancaire; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.credit_bancaire (
    recensement_id integer NOT NULL,
    type_credit_id integer NOT NULL
);


ALTER TABLE public.credit_bancaire OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 17773)
-- Name: financements; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.financements (
    recensement_id integer NOT NULL,
    type_financement_id integer NOT NULL
);


ALTER TABLE public.financements OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 17758)
-- Name: recensements; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recensements (
    id integer NOT NULL,
    nom_exploitant character varying(100),
    prenom character varying(100),
    wilaya character varying(100),
    commune character varying(100)
);


ALTER TABLE public.recensements OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 17757)
-- Name: recensements_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recensements_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.recensements_id_seq OWNER TO postgres;

--
-- TOC entry 4988 (class 0 OID 0)
-- Dependencies: 219
-- Name: recensements_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recensements_id_seq OWNED BY public.recensements.id;


--
-- TOC entry 229 (class 1259 OID 17823)
-- Name: soutien_public; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.soutien_public (
    recensement_id integer NOT NULL,
    type_soutien_id integer NOT NULL
);


ALTER TABLE public.soutien_public OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 17841)
-- Name: type_assurance_agricole; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_assurance_agricole (
    id integer NOT NULL,
    nom_fr character varying(150),
    nom_ar character varying(150)
);


ALTER TABLE public.type_assurance_agricole OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 17840)
-- Name: type_assurance_agricole_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_assurance_agricole_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.type_assurance_agricole_id_seq OWNER TO postgres;

--
-- TOC entry 4989 (class 0 OID 0)
-- Dependencies: 230
-- Name: type_assurance_agricole_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_assurance_agricole_id_seq OWNED BY public.type_assurance_agricole.id;


--
-- TOC entry 225 (class 1259 OID 17791)
-- Name: type_credit_bancaire; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_credit_bancaire (
    id integer NOT NULL,
    nom_fr character varying(150),
    nom_ar character varying(150)
);


ALTER TABLE public.type_credit_bancaire OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 17790)
-- Name: type_credit_bancaire_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_credit_bancaire_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.type_credit_bancaire_id_seq OWNER TO postgres;

--
-- TOC entry 4990 (class 0 OID 0)
-- Dependencies: 224
-- Name: type_credit_bancaire_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_credit_bancaire_id_seq OWNED BY public.type_credit_bancaire.id;


--
-- TOC entry 222 (class 1259 OID 17766)
-- Name: type_financement; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_financement (
    id integer NOT NULL,
    nom_fr character varying(150),
    nom_ar character varying(150)
);


ALTER TABLE public.type_financement OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 17765)
-- Name: type_financement_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_financement_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.type_financement_id_seq OWNER TO postgres;

--
-- TOC entry 4991 (class 0 OID 0)
-- Dependencies: 221
-- Name: type_financement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_financement_id_seq OWNED BY public.type_financement.id;


--
-- TOC entry 228 (class 1259 OID 17816)
-- Name: type_soutien_public; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_soutien_public (
    id integer NOT NULL,
    nom_fr character varying(150),
    nom_ar character varying(150)
);


ALTER TABLE public.type_soutien_public OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 17815)
-- Name: type_soutien_public_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_soutien_public_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.type_soutien_public_id_seq OWNER TO postgres;

--
-- TOC entry 4992 (class 0 OID 0)
-- Dependencies: 227
-- Name: type_soutien_public_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_soutien_public_id_seq OWNED BY public.type_soutien_public.id;


--
-- TOC entry 4791 (class 2604 OID 17761)
-- Name: recensements id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recensements ALTER COLUMN id SET DEFAULT nextval('public.recensements_id_seq'::regclass);


--
-- TOC entry 4795 (class 2604 OID 17844)
-- Name: type_assurance_agricole id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_assurance_agricole ALTER COLUMN id SET DEFAULT nextval('public.type_assurance_agricole_id_seq'::regclass);


--
-- TOC entry 4793 (class 2604 OID 17794)
-- Name: type_credit_bancaire id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_credit_bancaire ALTER COLUMN id SET DEFAULT nextval('public.type_credit_bancaire_id_seq'::regclass);


--
-- TOC entry 4792 (class 2604 OID 17769)
-- Name: type_financement id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_financement ALTER COLUMN id SET DEFAULT nextval('public.type_financement_id_seq'::regclass);


--
-- TOC entry 4794 (class 2604 OID 17819)
-- Name: type_soutien_public id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_soutien_public ALTER COLUMN id SET DEFAULT nextval('public.type_soutien_public_id_seq'::regclass);


--
-- TOC entry 4982 (class 0 OID 17848)
-- Dependencies: 232
-- Data for Name: assurances_agricoles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.assurances_agricoles (recensement_id, type_assurance_id) FROM stdin;
1	3
1	6
\.


--
-- TOC entry 4976 (class 0 OID 17798)
-- Dependencies: 226
-- Data for Name: credit_bancaire; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.credit_bancaire (recensement_id, type_credit_id) FROM stdin;
1	1
1	4
\.


--
-- TOC entry 4973 (class 0 OID 17773)
-- Dependencies: 223
-- Data for Name: financements; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.financements (recensement_id, type_financement_id) FROM stdin;
1	1
1	2
\.


--
-- TOC entry 4970 (class 0 OID 17758)
-- Dependencies: 220
-- Data for Name: recensements; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recensements (id, nom_exploitant, prenom, wilaya, commune) FROM stdin;
1	بن علي	أحمد	تيارت	تيارت
2	زروقي	فاطمة	الجزائر	الجزائر الوسطى
\.


--
-- TOC entry 4979 (class 0 OID 17823)
-- Dependencies: 229
-- Data for Name: soutien_public; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.soutien_public (recensement_id, type_soutien_id) FROM stdin;
1	1
1	2
\.


--
-- TOC entry 4981 (class 0 OID 17841)
-- Dependencies: 231
-- Data for Name: type_assurance_agricole; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_assurance_agricole (id, nom_fr, nom_ar) FROM stdin;
1	Terre	الأرض
2	Personnel	العمال
3	Cultures	المحاصيل
4	Bâtiments	المباني
5	Matériels	العتاد
6	Cheptel	المواشي
\.


--
-- TOC entry 4975 (class 0 OID 17791)
-- Dependencies: 225
-- Data for Name: type_credit_bancaire; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_credit_bancaire (id, nom_fr, nom_ar) FROM stdin;
1	Ettahadi	الاتحادي
2	Classique	كلاسيكي
3	Leasing	إيجار تمويلي
4	Rfig	رفيق
\.


--
-- TOC entry 4972 (class 0 OID 17766)
-- Dependencies: 222
-- Data for Name: type_financement; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_financement (id, nom_fr, nom_ar) FROM stdin;
1	Ressources propres	موارد ذاتية
2	Crédit bancaire	قرض بنكي
3	Soutien public	دعم عمومي
4	Emprunt à un tiers	قرض من الغير
\.


--
-- TOC entry 4978 (class 0 OID 17816)
-- Dependencies: 228
-- Data for Name: type_soutien_public; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_soutien_public (id, nom_fr, nom_ar) FROM stdin;
1	Financier	مالي
2	Matériel	عتاد
3	Cultures	محاصيل
\.


--
-- TOC entry 4993 (class 0 OID 0)
-- Dependencies: 219
-- Name: recensements_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recensements_id_seq', 2, true);


--
-- TOC entry 4994 (class 0 OID 0)
-- Dependencies: 230
-- Name: type_assurance_agricole_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_assurance_agricole_id_seq', 6, true);


--
-- TOC entry 4995 (class 0 OID 0)
-- Dependencies: 224
-- Name: type_credit_bancaire_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_credit_bancaire_id_seq', 4, true);


--
-- TOC entry 4996 (class 0 OID 0)
-- Dependencies: 221
-- Name: type_financement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_financement_id_seq', 4, true);


--
-- TOC entry 4997 (class 0 OID 0)
-- Dependencies: 227
-- Name: type_soutien_public_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_soutien_public_id_seq', 3, true);


--
-- TOC entry 4813 (class 2606 OID 17854)
-- Name: assurances_agricoles assurances_agricoles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assurances_agricoles
    ADD CONSTRAINT assurances_agricoles_pkey PRIMARY KEY (recensement_id, type_assurance_id);


--
-- TOC entry 4805 (class 2606 OID 17804)
-- Name: credit_bancaire credit_bancaire_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.credit_bancaire
    ADD CONSTRAINT credit_bancaire_pkey PRIMARY KEY (recensement_id, type_credit_id);


--
-- TOC entry 4801 (class 2606 OID 17779)
-- Name: financements financements_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financements
    ADD CONSTRAINT financements_pkey PRIMARY KEY (recensement_id, type_financement_id);


--
-- TOC entry 4797 (class 2606 OID 17764)
-- Name: recensements recensements_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recensements
    ADD CONSTRAINT recensements_pkey PRIMARY KEY (id);


--
-- TOC entry 4809 (class 2606 OID 17829)
-- Name: soutien_public soutien_public_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.soutien_public
    ADD CONSTRAINT soutien_public_pkey PRIMARY KEY (recensement_id, type_soutien_id);


--
-- TOC entry 4811 (class 2606 OID 17847)
-- Name: type_assurance_agricole type_assurance_agricole_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_assurance_agricole
    ADD CONSTRAINT type_assurance_agricole_pkey PRIMARY KEY (id);


--
-- TOC entry 4803 (class 2606 OID 17797)
-- Name: type_credit_bancaire type_credit_bancaire_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_credit_bancaire
    ADD CONSTRAINT type_credit_bancaire_pkey PRIMARY KEY (id);


--
-- TOC entry 4799 (class 2606 OID 17772)
-- Name: type_financement type_financement_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_financement
    ADD CONSTRAINT type_financement_pkey PRIMARY KEY (id);


--
-- TOC entry 4807 (class 2606 OID 17822)
-- Name: type_soutien_public type_soutien_public_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_soutien_public
    ADD CONSTRAINT type_soutien_public_pkey PRIMARY KEY (id);


--
-- TOC entry 4820 (class 2606 OID 17855)
-- Name: assurances_agricoles assurances_agricoles_recensement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assurances_agricoles
    ADD CONSTRAINT assurances_agricoles_recensement_id_fkey FOREIGN KEY (recensement_id) REFERENCES public.recensements(id);


--
-- TOC entry 4821 (class 2606 OID 17860)
-- Name: assurances_agricoles assurances_agricoles_type_assurance_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assurances_agricoles
    ADD CONSTRAINT assurances_agricoles_type_assurance_id_fkey FOREIGN KEY (type_assurance_id) REFERENCES public.type_assurance_agricole(id);


--
-- TOC entry 4816 (class 2606 OID 17805)
-- Name: credit_bancaire credit_bancaire_recensement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.credit_bancaire
    ADD CONSTRAINT credit_bancaire_recensement_id_fkey FOREIGN KEY (recensement_id) REFERENCES public.recensements(id);


--
-- TOC entry 4817 (class 2606 OID 17810)
-- Name: credit_bancaire credit_bancaire_type_credit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.credit_bancaire
    ADD CONSTRAINT credit_bancaire_type_credit_id_fkey FOREIGN KEY (type_credit_id) REFERENCES public.type_credit_bancaire(id);


--
-- TOC entry 4814 (class 2606 OID 17780)
-- Name: financements financements_recensement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financements
    ADD CONSTRAINT financements_recensement_id_fkey FOREIGN KEY (recensement_id) REFERENCES public.recensements(id);


--
-- TOC entry 4815 (class 2606 OID 17785)
-- Name: financements financements_type_financement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financements
    ADD CONSTRAINT financements_type_financement_id_fkey FOREIGN KEY (type_financement_id) REFERENCES public.type_financement(id);


--
-- TOC entry 4818 (class 2606 OID 17830)
-- Name: soutien_public soutien_public_recensement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.soutien_public
    ADD CONSTRAINT soutien_public_recensement_id_fkey FOREIGN KEY (recensement_id) REFERENCES public.recensements(id);


--
-- TOC entry 4819 (class 2606 OID 17835)
-- Name: soutien_public soutien_public_type_soutien_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.soutien_public
    ADD CONSTRAINT soutien_public_type_soutien_id_fkey FOREIGN KEY (type_soutien_id) REFERENCES public.type_soutien_public(id);


-- Completed on 2026-04-02 23:40:34

--
-- PostgreSQL database dump complete
--

\unrestrict Hxn7gRDTneYAlLvnRjTVxJvm3T4a9lrqpo53WT3zXu7803ESCmG6xtqIYZsWl05

