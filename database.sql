CREATE TABLE DIRECT_DEBITS
(
    ACCOUNT_NAME VARCHAR2(30),
    BALANCE VARCHAR2(30),
    STATEMENT_DATE DATE,
    BUFFER_DAYS NUMERIC,
    DD_DATE DATE,
    BANK VARCHAR2(10),
    CREDIT_LIMIT NUMERIC(10),
    CREDIT_PERCENT DECIMAL(6)
);

