USE RetirementClaimsDB;
GO

SELECT COUNT(*) AS total_records
FROM dbo.sqlserver_ready_claims;

SELECT TOP 10 *
FROM dbo.sqlserver_ready_claims;

SELECT
    category,
    COUNT(*) AS record_count
FROM dbo.sqlserver_ready_claims
GROUP BY category;

SELECT
    year,
    COUNT(*) AS record_count
FROM dbo.sqlserver_ready_claims
GROUP BY year
ORDER BY year;

SELECT
    life_insurer,
    COUNT(*) AS record_count
FROM dbo.sqlserver_ready_claims
GROUP BY life_insurer
ORDER BY record_count DESC;

SELECT
    COUNT(*) AS total_records,

    SUM(CASE WHEN life_insurer IS NULL THEN 1 ELSE 0 END) AS missing_insurer,

    SUM(CASE WHEN year IS NULL THEN 1 ELSE 0 END) AS missing_year,

    SUM(CASE WHEN category IS NULL THEN 1 ELSE 0 END) AS missing_category

FROM dbo.sqlserver_ready_claims;

SELECT *
FROM dbo.sqlserver_ready_claims
WHERE
    claims_pending_start_amt < 0
    OR claims_intimated_amt < 0
    OR total_claims_amt < 0
    OR claims_paid_amt < 0
    OR claims_repudiated_amt < 0
    OR claims_rejected_amt < 0
    OR claims_unclaimed_amt < 0
    OR claims_pending_end_amt < 0;