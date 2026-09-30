CREATE DATABASE RetirementClaimsDB;

USE RetirementClaimsDB;

CREATE TABLE RetirementClaims (
    record_id INT IDENTITY(1,1) PRIMARY KEY,

    id INT NULL,

    life_insurer NVARCHAR(255) NULL,

    year NVARCHAR(20) NULL,

    category NVARCHAR(50) NULL,

    claims_pending_start_no INT NULL,

    claims_pending_start_amt DECIMAL(18,2) NULL,

    claims_intimated_no INT NULL,

    claims_intimated_amt DECIMAL(18,2) NULL,

    total_claims_no INT NULL,

    total_claims_amt DECIMAL(18,2) NULL,

    claims_paid_no INT NULL,

    claims_paid_amt DECIMAL(18,2) NULL,

    claims_repudiated_no INT NULL,

    claims_repudiated_amt DECIMAL(18,2) NULL,

    claims_rejected_no INT NULL,

    claims_rejected_amt DECIMAL(18,2) NULL,

    claims_unclaimed_no INT NULL,

    claims_unclaimed_amt DECIMAL(18,2) NULL,

    claims_pending_end_no INT NULL,

    claims_pending_end_amt DECIMAL(18,2) NULL,

    claims_paid_ratio_no DECIMAL(10,2) NULL,

    claims_paid_ratio_amt DECIMAL(10,2) NULL,

    claims_repudiated_rejected_ratio_no DECIMAL(10,2) NULL,

    claims_repudiated_rejected_ratio_amt DECIMAL(10,2) NULL,

    claims_pending_ratio_no DECIMAL(10,2) NULL,

    claims_pending_ratio_amt DECIMAL(10,2) NULL
);


SELECT *
FROM RetirementClaims;

USE RetirementClaimsDB;
GO

SELECT COUNT(*) AS total_records
FROM dbo.sqlserver_ready_claims;

INSERT INTO dbo.RetirementClaims
(
    id,
    life_insurer,
    year,
    category,
    claims_pending_start_no,
    claims_pending_start_amt,
    claims_intimated_no,
    claims_intimated_amt,
    total_claims_no,
    total_claims_amt,
    claims_paid_no,
    claims_paid_amt,
    claims_repudiated_no,
    claims_repudiated_amt,
    claims_rejected_no,
    claims_rejected_amt,
    claims_unclaimed_no,
    claims_unclaimed_amt,
    claims_pending_end_no,
    claims_pending_end_amt,
    claims_paid_ratio_no,
    claims_paid_ratio_amt,
    claims_repudiated_rejected_ratio_no,
    claims_repudiated_rejected_ratio_amt,
    claims_pending_ratio_no,
    claims_pending_ratio_amt
)

SELECT
    id,
    life_insurer,
    year,
    category,
    claims_pending_start_no,
    claims_pending_start_amt,
    claims_intimated_no,
    claims_intimated_amt,
    total_claims_no,
    total_claims_amt,
    claims_paid_no,
    claims_paid_amt,
    claims_repudiated_no,
    claims_repudiated_amt,
    claims_rejected_no,
    claims_rejected_amt,
    claims_unclaimed_no,
    claims_unclaimed_amt,
    claims_pending_end_no,
    claims_pending_end_amt,
    claims_paid_ratio_no,
    claims_paid_ratio_amt,
    claims_repudiated_rejected_ratio_no,
    claims_repudiated_rejected_ratio_amt,
    claims_pending_ratio_no,
    claims_pending_ratio_amt
FROM dbo.sqlserver_ready_claims;

SELECT
    COLUMN_NAME,
    DATA_TYPE,
    ORDINAL_POSITION
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'sqlserver_ready_claims'
ORDER BY ORDINAL_POSITION;


SELECT TOP 5 *
FROM dbo.sqlserver_ready_claims;
