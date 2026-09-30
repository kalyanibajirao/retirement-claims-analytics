USE RetirementClaimsDB;

--Claim Summary

CREATE OR ALTER VIEW dbo.vw_claim_summary
AS
SELECT
    COUNT(*) AS total_records,

    SUM(total_claims_no) AS total_claims,

    SUM(total_claims_amt) AS total_claim_amount,

    SUM(claims_paid_no) AS paid_claims,

    SUM(claims_paid_amt) AS paid_claim_amount,

    SUM(claims_pending_end_no) AS pending_claims,

    SUM(claims_pending_end_amt) AS pending_claim_amount,

    SUM(claims_repudiated_no) AS repudiated_claims,

    SUM(claims_rejected_no) AS rejected_claims,

    SUM(claims_unclaimed_no) AS unclaimed_claims

FROM dbo.sqlserver_ready_claims;

SELECT *
FROM dbo.vw_claim_summary;

--Claim Status

CREATE OR ALTER VIEW dbo.vw_claim_status
AS

SELECT
    'Paid' AS claim_status,
    SUM(claims_paid_no) AS claim_count,
    SUM(claims_paid_amt) AS claim_amount
FROM dbo.sqlserver_ready_claims

UNION ALL

SELECT
    'Pending' AS claim_status,
    SUM(claims_pending_end_no) AS claim_count,
    SUM(claims_pending_end_amt) AS claim_amount
FROM dbo.sqlserver_ready_claims

UNION ALL

SELECT
    'Repudiated' AS claim_status,
    SUM(claims_repudiated_no) AS claim_count,
    SUM(claims_repudiated_amt) AS claim_amount
FROM dbo.sqlserver_ready_claims

UNION ALL

SELECT
    'Rejected' AS claim_status,
    SUM(claims_rejected_no) AS claim_count,
    SUM(claims_rejected_amt) AS claim_amount
FROM dbo.sqlserver_ready_claims;

SELECT *
FROM dbo.vw_claim_status;

--Group vs Individual

CREATE OR ALTER VIEW dbo.vw_claim_type
AS
SELECT
    category,

    COUNT(*) AS record_count,

    SUM(total_claims_no) AS total_claims,

    SUM(total_claims_amt) AS total_claim_amount,

    SUM(claims_paid_no) AS paid_claims,

    SUM(claims_paid_amt) AS paid_claim_amount,

    SUM(claims_pending_end_no) AS pending_claims,

    SUM(claims_pending_end_amt) AS pending_claim_amount,

    SUM(claims_rejected_no) AS rejected_claims,

    SUM(claims_repudiated_no) AS repudiated_claims

FROM dbo.sqlserver_ready_claims

GROUP BY category;

SELECT *
FROM dbo.vw_claim_type;

--Yearly Performance

CREATE OR ALTER VIEW dbo.vw_claim_yearly
AS
SELECT
    year,

    SUM(total_claims_no) AS total_claims,

    SUM(total_claims_amt) AS total_claim_amount,

    SUM(claims_paid_no) AS paid_claims,

    SUM(claims_paid_amt) AS paid_claim_amount,

    SUM(claims_pending_end_no) AS pending_claims,

    SUM(claims_pending_end_amt) AS pending_claim_amount,

    SUM(claims_rejected_no) AS rejected_claims,

    SUM(claims_repudiated_no) AS repudiated_claims,

    SUM(claims_unclaimed_no) AS unclaimed_claims

FROM dbo.sqlserver_ready_claims

GROUP BY year;

SELECT *
FROM dbo.vw_claim_yearly;

--Insurer Performance

CREATE OR ALTER VIEW dbo.vw_insurer_performance
AS
SELECT
    life_insurer,

    COUNT(*) AS record_count,

    SUM(total_claims_no) AS total_claims,

    SUM(total_claims_amt) AS total_claim_amount,

    SUM(claims_paid_no) AS paid_claims,

    SUM(claims_paid_amt) AS paid_claim_amount,

    SUM(claims_pending_end_no) AS pending_claims,

    SUM(claims_pending_end_amt) AS pending_claim_amount,

    SUM(claims_rejected_no) AS rejected_claims,

    SUM(claims_repudiated_no) AS repudiated_claims,

    SUM(claims_unclaimed_no) AS unclaimed_claims

FROM dbo.sqlserver_ready_claims

GROUP BY life_insurer;

SELECT *
FROM dbo.vw_insurer_performance
ORDER BY total_claim_amount DESC;

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.VIEWS
WHERE TABLE_SCHEMA = 'dbo'
ORDER BY TABLE_NAME;

SELECT *
FROM dbo.vw_claim_summary;

SELECT *
FROM dbo.vw_claim_status;

SELECT *
FROM dbo.vw_claim_type;

SELECT *
FROM dbo.vw_claim_yearly;

SELECT *
FROM dbo.vw_insurer_performance;