

/*

Goal: Identify the top 3 customers by total purchase amount in each sales territory, based on completed orders.


- Sales.SalesOrderHeader — contains order info
- Sales.SalesOrderDetail — line items and prices
- Sales.Customer — customer info
- Sales.SalesTerritory — region info

- Only include orders with Status = 5 (completed).
- Sum LineTotal from SalesOrderDetail per customer.
- Partition by TerritoryID and rank customers by total spend.
- Return top 3 per territory, showing:
- Territory Name
- Customer ID
- Total Purchase Amount
- Rank

*/

IF OBJECT_ID('tempdb..#tmp_results ', 'U') IS NOT NULL
/*Then it exists*/
DROP TABLE #tmp_results 



;WITH CustomerTotals AS (
    SELECT
        soh.CustomerID,
        soh.TerritoryID,
        SUM(sod.LineTotal) AS TotalSpent
    FROM Sales.SalesOrderHeader soh
    JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
    WHERE soh.Status = 5
    GROUP BY soh.CustomerID, soh.TerritoryID
),
RankedCustomers AS (
    SELECT
        ct.CustomerID,
        st.Name AS Territory,
        ct.TotalSpent,
        RANK() OVER (PARTITION BY ct.TerritoryID ORDER BY ct.TotalSpent DESC) AS Rank
    FROM CustomerTotals ct
    JOIN Sales.SalesTerritory st ON ct.TerritoryID = st.TerritoryID
)
SELECT *
INTO #tmp_results 
FROM [RankedCustomers]
WHERE Rank <= 3
ORDER BY [Territory],[Rank]

SELECT * FROM #tmp_results